from db.serializers.cart_serializer import CartSerializer, CartCourseSerializer
from db.models.cart import Cart
from lib.response import Response
from db.models.course import Course
from api.permissions.cart_permissions import CartOwner

from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404


class CartDetail(APIView):
    serializer_class = CartSerializer
    permission_classes = (permissions.IsAuthenticated, CartOwner)
    
    def get_object(self, pk):
        try:
            return Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        cart_id=self.get_object(pk)
        serializer = CartCourseSerializer(cart_id)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk, format=None):
        cart = self.get_object(pk)
        self.check_object_permissions(request, cart)
        cart.delete()
        return Response(data={"data":{}},status=status.HTTP_204_NO_CONTENT)
