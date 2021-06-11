from decouple import config
from rest_framework import permissions, status
from rest_framework.generics import ListCreateAPIView

from db.models.blogs import Blog
from lib.response import Response
from lib.cloudinary_interface import CloudinaryInterface
from db.serializers.blog_serializer import BlogSerializer, BlogListSerializer


class Blogs(ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def create(self, request):
        cover_img = request.data.get('cover_img', '')

        if not cover_img:
            return Response(errors=dict(cover_img="Please provide a cover image"))

        data = request.data
        data['user_id'] = request.user.id

        serializer = self.serializer_class(data=data)
        if not serializer.is_valid():
            return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        cover_img_url = CloudinaryInterface.upload_image(
            cover_img, folder_name=config('CLOUD_BLOG_FOLDER'))

        if not cover_img_url:
            return Response(errors=dict(invalid_cover_img="Image upload failed, please make sure you are uploading a valid image format"))

        get_cover_img_url = cover_img_url.get('url')

        serializer.save(cover_img=get_cover_img_url)
        serializer_dict = dict(serializer.data)
        serializer_dict['cover_img'] = get_cover_img_url

        return Response(data={
            "blogs": serializer_dict,
            "total": self.queryset.count(),
        },
            status=status.HTTP_201_CREATED,
        )

    def list(self, request):
        queryset = Blog.objects.all().order_by('-created_at')
        serializer_class = BlogListSerializer(data=queryset, many=True)
        serializer_class.is_valid()
        return Response(
            data={
                "blogs": serializer_class.data,
                "total": self.queryset.count(),
            },
            status=status.HTTP_200_OK,
        )
