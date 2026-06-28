from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import ThreeSumSerializer

class ThreeSumView(APIView):
    def(self, request):
        serializer = ThreeSumSerializer(data=request.data)
        pass
