from rest_framework import generics, permissions

from . import models, serializers


class UserTasksView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.UserTasksSerializer

    def get_queryset(self):
        return models.UserTask.objects.filter(user__id=self.request.user.id)


class UserTaskCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.UserTasksSerializer
    queryset = models.UserTask.objects.all()
