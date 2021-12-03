from rest_framework import generics, status, permissions
from rest_framework.response import Response

from . import serializers, models


class EmployeeListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny, ]
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()


class EmployeeInfoView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.EmployeeSerializer
    queryset = models.Employee.objects.all()


class LogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Пользователь вышел"},
                        status=status.HTTP_204_NO_CONTENT)
