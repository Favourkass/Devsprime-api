from db.models.learner_course import LearnerCourse
from db.models.course import Course
from rest_framework import generics, permissions, status
from lib.response import Response
from db.models.course_payment import CoursePayment
from db.models.order_status import OrderStatus
from db.models.orders import Order
from db.serializers.course_payment_serializer import CoursePaymentInputSerializer
from db.models.learner import LearnerProfile



class CoursePaymentView(generics.GenericAPIView):    
    permission_classes = (permissions.IsAuthenticated,) 
    serializer_class = (CoursePaymentInputSerializer,)
    queryset = CoursePayment.objects.all()

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:            
            return Response({"email": f'{request.user.email}'})
        return Response(None, {'email': ''})

    def post(self, request, *args, **kwargs):        
        serializer = CoursePaymentInputSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True): 
            learner = LearnerProfile.objects.get(user_id=self.request.user)
            get_course = Course.objects.get(id=serializer.data.get('course_id'))
            get_paystack_ref=serializer.data.get('paystack_id')
            get_order_status = OrderStatus.objects.create(name='pending')
            # create New Order
            get_order = Order.objects.create(
                course_id=get_course,
                learner_id=learner,
                order_status_id=get_order_status
            )             
            if get_paystack_ref == "declined":
                 # update order status to unsuccessful
                get_order_status.name='unsuccessful'               
                get_order_status.reason='payment failed'               
                get_order_status.save()   
                return Response(errors=dict(payment_error=get_paystack_ref), status=status.HTTP_400_BAD_REQUEST)

            # create New CoursePayment
            CoursePayment.objects.create(
            course_id=get_course,
            learner_id=learner,
            order_id=get_order,
            paystack_id=get_paystack_ref,
            amount=float(get_course.price)
            )     
            # update order status to successful         
            get_order_status.name='successful'               
            get_order_status.save()
            # Add course to the learners course
            LearnerCourse.objects.create(learner_id=learner, course_id=get_course)
            return Response(data=serializer.data, status=status.HTTP_200_OK)   
        return Response(None, {'Invalid request': 'Please enter valid input data'})
