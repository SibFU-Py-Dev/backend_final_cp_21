from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import ProjectSerializer
from .models import Project

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all().select_related()
