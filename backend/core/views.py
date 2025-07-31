from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
import pandas as pd
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser

class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    @action(detail=True, methods=['get'])
    def tasks(self, request, pk=None):
        project_tasks = Task.objects.filter(project_id=pk)
        serializer = TaskSerializer(project_tasks, many=True)
        return Response(serializer.data)
    
class TaskModelViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        queryset = Task.objects.all()
        project_id = self.request.query_params.get('project')
        if project_id:
            queryset = queryset.filter(project_id=project_id)
        return queryset
    
@api_view(['POST'])
@parser_classes([MultiPartParser])
def import_tasks(request):
    file = request.FILES.get('file')
    if not file:
        return Response({'error': 'No file provided'}, status=400)

    try:
        df = pd.read_excel(file)  # assumes file is .xlsx
        for _, row in df.iterrows():
            # Adjust column names to match your Excel file headers
            project_name = row.get('project')
            project, _ = Project.objects.get_or_create(name=project_name)

            Task.objects.create(
                name=row.get('name'),
                description=row.get('description'),
                project=project,
                parent_id=row.get('parent_id') if not pd.isna(row.get('parent_id')) else None
            )
        return Response({'message': 'Tasks imported successfully'})
    except Exception as e:
        return Response({'error': str(e)}, status=400)