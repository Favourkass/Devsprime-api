from decouple import config
from django.contrib.auth import get_user_model
from rest_framework import views, permissions, status
from rest_framework.parsers import MultiPartParser, JSONParser, FormParser

from lib.response import Response
from lib.cloudinary_interface import CloudinaryInterface
from db.serializers.user_serializer import UserSerializer, UserProfileSerializer


class User(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer
    parser_classes = (MultiPartParser, JSONParser, FormParser)

    def get(self, request):
        current_user = get_user_model().objects.get(id=request.user.id)
        serializer = UserSerializer(current_user)
        return Response(data={**serializer.data}, status=status.HTTP_200_OK)

    def put(self, request, format=None):
        avatar = request.data.get('avatar', '')
        current_user = get_user_model().objects.get(id=request.user.id)
        if not avatar:
            serializer = UserProfileSerializer(
                current_user, data=request.data, partial=True)
            if not serializer.is_valid():
                return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            output_serializer = UserSerializer(current_user)
            return Response(data={**output_serializer.data}, status=status.HTTP_200_OK)

        avatar_url = CloudinaryInterface.upload_image(
            avatar, folder_name=config('CLOUD_AVATAR_FOLDER'))
        if not avatar_url:
            return Response(
                errors=dict(
                    invalid_avatar="Image upload failed, please make sure you are uploading a valid image format")
            )
        get_avatar = avatar_url.get('url')
        data = request.data
        data['avatar'] = get_avatar
        serializer = UserProfileSerializer(
            current_user, data=data, partial=True)
        if not serializer.is_valid():
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save(avatar=get_avatar)
        output_serializer = UserSerializer(current_user)
        return Response(data={**output_serializer.data}, status=status.HTTP_200_OK)


class Users(views.APIView):
    def get(self, request):
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(data=dict(users=serializer.data, total=len(serializer.data)), status=status.HTTP_200_OK)
