from rest_framework import serializers
from db.models.course_payment import CoursePayment


class CoursePaymentInputSerializer(serializers.Serializer):
    course_id = serializers.CharField()        
    paystack_id = serializers.CharField()
