from rest_framework import serializers
from db.models.comment import  Comment
from db.models.reply import  Reply


class ReplySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Reply
        fields = [ 'id', 'comment_id','reply','created_at','updated_at']


class CommentSerializer(serializers.ModelSerializer):
    name = serializers.ReadOnlyField(source='user_id.fullname')
    reply = ReplySerializer(many=True, read_only=True)
    
    class Meta:
        model = Comment
        fields = ( 'id', 'blog_id','name','comment','created_at','updated_at','reply',)

