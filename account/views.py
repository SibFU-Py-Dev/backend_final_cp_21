from rest_framework import generics, status, permissions, views
from rest_framework.response import Response
from . import serializers


class LogoutAPIView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = serializers.LogoutSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Пользователь вышел"},
                        status=status.HTTP_204_NO_CONTENT)
