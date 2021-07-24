from rest_framework import serializers
from db.models.blogs import Blog


class BlogSerializer(serializers.ModelSerializer):
    fullname = serializers.ReadOnlyField(source='user_id.fullname')

    class Meta:
        model = Blog
        fields = ['id', 'user_id', 'fullname', 'title', 'short_desc', 'detail', 'created_at', 'updated_at']

class BlogListSerializer(serializers.ModelSerializer):
    fullname = serializers.ReadOnlyField(source='user_id.fullname')

    class Meta:
        model = Blog
        fields = ['id', 'user_id','cover_img', 'fullname', 'title', 'short_desc', 'detail', 'created_at', 'updated_at']
