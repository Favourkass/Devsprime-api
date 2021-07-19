from rest_framework import serializers

from .comment_serializer import CommentSerializers
from db.models.blogs import Blog


class BlogSerializers(serializers.ModelSerializer):
    
    
    comments = CommentSerializers(many=True, read_only=True)
    fullname = serializers.ReadOnlyField(source='user_id.fullname')
    class Meta:
        model = Blog
        fields = ('id', 'user_id','fullname','title','cover_img','short_desc','detail','created_at','updated_at','comments')