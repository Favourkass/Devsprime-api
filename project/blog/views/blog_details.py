from django.http import Http404, response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status

from blog.permissions.is_author import IsAuthorOrReadOnly
from db.models.blogs import Blog
from ..serializers.blog_serializer import BlogSerializers

from lib.response import Response

        
class BlogDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly, ]
    serializer_class = BlogSerializers
    
    def get_object(self, uuid):
        try:
            return Blog.objects.get(pk=uuid)
        except Blog.DoesNotExist:
            raise Http404
        

    def get(self, request, uuid, format=None):
        blog = self.get_object(uuid)
        serializer = BlogSerializers(blog)
      
        return Response(data={
            "blog": serializer.data,
             },
            status=status.HTTP_200_OK,
        )

    def put(self, request, uuid, format=None):
        blog = self.get_object(uuid)
        serializer = BlogSerializers(blog, data=request.data, partial=True)
        self.check_object_permissions(request, blog)
        if serializer.is_valid():
            serializer.save()
            return Response(data= serializer.data,status=status.HTTP_200_OK)
         
        return Response(errors=serializer.errors,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, uuid, format=None):
        blog = self.get_object(uuid)
        self.check_object_permissions(request, blog)
        blog.delete()
        return Response(data={"data":{}},status=status.HTTP_204_NO_CONTENT)
       
