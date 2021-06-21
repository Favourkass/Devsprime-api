from db.models.learner import LearnerProfile
from db.serializers.cart_serializer import CartSerializer, CartCourseSerializer
from db.models.cart import Cart
from lib.response import Response
from db.models.course import Course

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView


class CartItemList(APIView):
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request, format=None):
        """This method get all courses in the user cart"""
        learner = LearnerProfile.objects.get(user_id=request.user.id)
        cart_item = Cart.objects.filter(learner_id=learner.id)
        serializer = CartCourseSerializer(cart_item, many=True)
        total = len(serializer.data)
        return Response(dict(Courses=serializer.data, Total=total), status=status.HTTP_200_OK)
    
    def post(self, request, format=None):
        """This method add a course to the current user cart and create a new cart for users without a cart"""
        user_id = request.user.id
        learner = LearnerProfile.objects.get(user_id=user_id)
        request.data['learner_id'] = learner.id
        
        serializer = CartSerializer(data=request.data)

        if serializer.is_valid():
            courseprofile_id= serializer.data.get("course_id")
            course_id = Course.objects.get(id=(courseprofile_id))

            if not Cart.objects.filter(learner_id=learner, course_id=course_id).exists():
                courses = Cart.objects.create(learner_id=learner, course_id=course_id)
            course = Cart.objects.get(learner_id=learner, course_id=course_id)
            courses_details = CartSerializer(course)
            return Response({'Courses': courses_details.data}, status=status.HTTP_201_CREATED)
        return Response(errors=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
