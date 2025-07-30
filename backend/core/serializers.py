from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model= Project
        fields= '_all_'

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model= Task
        fields= '_all_'