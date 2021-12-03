from rest_framework import serializers

from account.serializers import UserSerializer
from . import models


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = "__all__"


class UserTasksSerializer(serializers.ModelSerializer):
    task = TaskSerializer(many=True)
    user = UserSerializer()
    responsible = UserSerializer()

    class Meta:
        model = models.UserTask
        fields = ['deadline', 'perfect_deadline', 'task', 'user', 'responsible', 'status', 'estimation', 'description']
