from rest_framework.viewsets import ModelViewSet
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

class MyView(ModelViewSet):

    def test(self, request, *args, **kwargs):
        return Response({"message": "It works!"}, status=status.HTTP_200_OK)