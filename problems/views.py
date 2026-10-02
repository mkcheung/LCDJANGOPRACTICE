from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Problem, Submission

from .serializers import (
    ContainerOfWaterSerializer,
    LongestIncreasingSubsequenceSerializer,
    LongestNonRepeatingSubstringSerializer,
    LongestPalindromeSerializer,
    ProblemListSerializer,
    ProductOfArrayExceptSelfSerializer,
    ThreeSumSerializer,
    TwoSumSerializer,
    TrappedRainwaterSerializer,
    ValidParenthesisSerializer,
)

class ProblemListView(APIView):
    def get(self, request):
        problems = Problem.objects.order_by('leetcode_number')
        serializer = ProblemListSerializer(problems, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ThreeSumView(APIView):
    def post(self, request):
        serializer = ThreeSumSerializer(data=request.data)
        if serializer.is_valid():
            problem, _ = Problem.objects.get_or_create(slug="three_sum", defaults={"title": "THREE SUM", "leetcode_number":15, "difficulty": "MEDIUM"})
            result = serializer.save()
            submission = Submission.objects.create(problem=problem, input_data=serializer.validated_data, result=result)

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
            problem, _ = Problem.objects.get_or_create(slug="two_sum", defaults={"title": "TWO SUM", "leetcode_number": 1, "difficulty": "EASY"})
            result = serializer.save()
            submission = Submission.objects.create(problem=problem, input_data=serializer.validated_data, result=result)

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
            problem, _ = Problem.objects.get_or_create(slug="longest_non_repeating_substring_view", defaults={"title": "LONGEST REPEATING SUBSTRING", "leetcode_number":3, "difficulty":"MEDIUM"})
            result = serializer.save()
            submission = Submission.objects.create(problem=problem, input_data=serializer.validated_data, result=result)

            return Response(
                result,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LongestPalindromeView(APIView):
    def post(self, request):
        serializer = LongestPalindromeSerializer(data=request.data)
        if serializer.is_valid():
            problem, _ = Problem.objects.get_or_create(slug="longest_palindrome", defaults={"title":"LONGEST PALINDROME", "leetcode_number": 5, "difficulty": "MEDIUM"})
            result = serializer.save()
            submission = Submission.objects.create(problem=problem, input_data=serializer.validated_data, result=result)

            return Response(
                result,
                status = status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LongestIncreasingSubsequenceView(APIView):
    def post(self, request):
        serializer = LongestIncreasingSubsequenceSerializer(data=request.data)
        if serializer.is_valid():
            problem, _ = Problem.objects.get_or_create(slug="longest_increasing_subsequence", defaults={"title":"LONGEST INCREASING SUBSEQUENCE", "leetcode_number": 300, "difficulty": "MEDIUM"})
            result = serializer.save()
            submimssion = Submission.objects.create(problem=problem, input_data=serializer.validated_data, result=result)

            return Response(
                result,
                status = status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ValidParenthesisView(APIView):
    def post(self, request):
        serializer = ValidParenthesisSerializer(data=request.data)
        if serializer.is_valid():
            problem, _ = Problem.objects.get_or_create(slug="valid_parenthesis", defaults={"title":"Valid Parenthesis", "leetcode_number": 20, "difficulty": "EASY"})
            result = serializer.save()
            submission = Submission.objects.create(problem=problem, input_data = serializer.validated_data, result=result)
            
            return Response(
                result,
                status = status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class TrappedRainwaterView(APIView):
    def post(self, request):
        serializer = TrappedRainwaterSerializer(data=request.data)
        if serializer.is_valid():
            problem, _ = Problem.objects.get_or_create(slug="trapped_rainwater", defaults={"title":"Trapped Rainwater", "leetcode_number": 42, "difficulty": "HARD"})
            result = serializer.save()
            submission = Submission.objects.create(problem=problem, input_data = serializer.validated_data, result=result)

            return Response(
                result,
                status = status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ProductOfArrayExceptSelfView(APIView):
    def post(self, request):
        
        serializer = ProductOfArrayExceptSelfSerializer(data=request.data)

        if serializer.is_valid():
            problem, _ = Problem.objects.get_or_create(slug="product_of_array_except_self", defaults={"title":"Product of Array Except Self", "leetcode_number": 238, "difficulty":"MEDIUM"})
            result = serializer.save()
            submission = Submission.objects.create(problem=problem, input_data = serializer.validated_data, result=result)

            return Response(
                result, 
                status = status.HTTP_200_OK
            )
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class ContainerOfWaterView(APIView):
    def post(self, request):
        
        serializer = ContainerOfWaterSerializer(data = request.data)

        if serializer.is_valid():
            problem, _ = Problem.objects.get_or_create(slug="container_of_water", defaults={"title":"Container of Water", "leetcode_number":11, 'difficulty':'MEDIUM'})
            result = serializer.save()
            submission = Submission.objects.create(problem=problem, input_data = serializer.validated_data, result=result)

            return Response(
                result,
                status = status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )