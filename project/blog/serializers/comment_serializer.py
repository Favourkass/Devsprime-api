from rest_framework import serializers
from .reply_serializer import ReplySerializers
from db.models.comment import Comment


class CommentSerializers(serializers.ModelSerializer):
    

    replies = ReplySerializers(many=True, read_only=True)
   
    class Meta:
        model = Comment
        fields = ( 'id', 'blog_id','comment','created_at','updated_at','replies',)

