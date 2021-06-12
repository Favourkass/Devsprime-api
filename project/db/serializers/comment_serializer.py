from rest_framework import serializers
from db.models.comment import Comment
from db.models.user import User


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='user_id.email')
    blog_id = serializers.ReadOnlyField(source='blog_id.id')

    class Meta:
        model = Comment
        fields = ['id', 'owner', 'blog_id', 'comment', 'created_at','updated_at']
