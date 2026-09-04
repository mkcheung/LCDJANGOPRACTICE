from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from models import Problem

from .serializers import TwoSumSerializer, ThreeSumSerializer, LongestNonRepeatingSubstringSerializer

class ThreeSumView(APIView):
    def post(self, request):
        serializer = ThreeSumSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()

            return Response(
                result,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class TwoSumView(APIView):
    def post(self, request):
        serializer = TwoSumSerializer(data=request.data)
        if serializer.is_valid():
            problem = Problem.objects.get_or_create(slug="two_sum", title="TWO SUM", leetcode_number=1, difficulty="EASY")
            result = serializer.save()

            return Response(
                result,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LongestNonRepeatingSubstringView(APIView):
    def post(self, request):
        serializer = LongestNonRepeatingSubstringSerializer(data=request.data)
        if serializer.is_valid():
            result = serializer.save()

            return Response(
                result,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )