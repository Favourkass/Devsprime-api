from rest_framework import serializers
from db.models.cart import Cart


class CartCourseSerializer(serializers.ModelSerializer):
    # course = serializers.StringRelatedField(many=True, read_only=True)
    title = serializers.PrimaryKeyRelatedField(
        read_only=True, source='course_id.title')
    description = serializers.PrimaryKeyRelatedField(
        read_only=True, source='course_id.description')
    cover_img = serializers.PrimaryKeyRelatedField(
        read_only=True, source='course_id.cover_img')
    instructor_name = serializers.PrimaryKeyRelatedField(
        read_only=True, source='course_id.instructor_id.user_id.fullname')
    price = serializers.PrimaryKeyRelatedField(
        read_only=True, source='course_id.price')
    course_type = serializers.PrimaryKeyRelatedField(
        read_only=True, source='course_id.type_id.name')

    class Meta:
        model = Cart
        fields = ['id', 'title', 'description', 'cover_img', 'price', 'course_type',
                  'instructor_name', 'created_at', 'updated_at']


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id',  'learner_id', 'course_id', 'created_at', 'updated_at']
