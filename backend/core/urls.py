from django.urls import path
from .views import ProjectModelViewSet, TaskModelViewSet

urlpatterns = [
    # Projects
    path("projects/", ProjectModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='project-list'),
    
    path("projects/<int:pk>/", ProjectModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='project-detail'),

    # Tasks
    path("tasks/", TaskModelViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='task-list'),
    
    path("tasks/<int:pk>/", TaskModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='task-detail'),
]
