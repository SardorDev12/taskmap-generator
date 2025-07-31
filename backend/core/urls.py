from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProjectModelViewSet, TaskModelViewSet

urlpatterns = [
    path("projects/", ProjectModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='project-list'),
    path("tasks/", TaskModelViewSet.as_view({'get': 'list', 'post': 'create'}), name='task-list'),
  
]