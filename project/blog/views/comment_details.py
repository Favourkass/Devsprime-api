from rest_framework.views import APIView
from django.http import Http404
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from db.models.comment import Comment
from db.models.reply import Reply
from blog.serializers.comment_serializer import CommentSerializers
from rest_framework import status
from blog.permissions.is_author import IsAuthorOrReadOnly
from lib.response import Response



class CommentDetails(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    def get_object(self, pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404
  
    def length_of_replies(self,pk):
        reply = Reply.objects.filter(comment_id=pk)
        return len(reply)

    def get(self, request, pk, format=None):
        comment_id = self.get_object(pk)
        serializer = CommentSerializers(comment_id)
        return Response(dict(serializer.data, total=self.length_of_replies(pk)))


    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        self.check_object_permissions(request, comment)

        serializer = CommentSerializers(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(errors=serializer.errors,status=status.HTTP_404_NOT_FOUND)


    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response(data={"data":{}},
            status=status.HTTP_204_NO_CONTENT,
        )
