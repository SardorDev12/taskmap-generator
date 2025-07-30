from rest_framework import viewsets
from .models import Project, Task
from .serializers import ProjectSerializer, TaskSerializer

class ProjectModelViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()