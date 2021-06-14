from db.models.orders import Order
from db.models.learner import LearnerProfile
from db.serializers.orders_serializer import OrderSerializer
from rest_framework import permissions,views,status
from lib.response import Response


class OrderListView(views.APIView):
    permission_classes=(permissions.IsAuthenticated,)
    serializer_class = OrderSerializer

    def get(self,request):
        
        user = self.request.user.id
        learner_id = LearnerProfile.objects.filter(user_id=user)
        if not learner_id:
            return Response(errors=dict(invalid_user="only learner can have a course"), status=status.HTTP_400_BAD_REQUEST)
        learner_id=learner_id.get().id
        order_queryset = Order.objects.filter(learner_id=learner_id)
        response_data = [{"id":order.course_id.id,
                            "title":order.course_id.title,
                            "description":order.course_id.description,
                            "cover_img":order.course_id.cover_img,
                            "category":order.course_id.category_id.name,
                            "created_at":order.course_id.created_at,
                            "updated_at":order.course_id.updated_at
                            } for order in order_queryset
                        ]
        response = {"courses":response_data,"total":len(response_data)}
        return Response(data=response, status=status.HTTP_200_OK)
        
            