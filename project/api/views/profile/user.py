from django.contrib.auth import get_user_model
from rest_framework import views, permissions, status

from lib.response import Response
from db.serializers.user_serializer import UserSerializer


class User(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        current_user = get_user_model().objects.get(id=request.user.id)
        serializer = UserSerializer(current_user)
        return Response(data={**serializer.data}, status=status.HTTP_200_OK)


class Users(views.APIView):
    def get(self, request):
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=dict(users=serializer.data, total=len(serializer.data)), status=status.HTTP_200_OK)
