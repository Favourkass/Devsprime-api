from rest_framework.views import APIView
from lib.response import Response
from rest_framework import authentication
from rest_framework import permissions
from db.models.comment import Comment
from db.models.blogs import Blog
from db.serializers.comment_serializer import CommentSerializer


class CommentView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        queryset = Comment.objects.filter(blog_id=blog)
        length = len(queryset)
        serializer = CommentSerializer(queryset, many=True, context={'request' : request})
        return Response(dict(data=serializer.data, total=length))

    def post(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        serializer = CommentSerializer(data=request.data, context={'request' : request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=request.user, blog_id=blog)
        return Response(serializer.data)
