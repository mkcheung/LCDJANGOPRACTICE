from django.urls import path

from .views import TwoSumView, ThreeSumView, LongestNonRepeatingSubstringView, LongestPalindromeView, LongestIncreasingSubsequence, ValidParenthesis, TrappedRainwater, ProductOfArrayExceptSelf, ContainerOfWater

urlpatterns = [
    path('two-sum/', TwoSumView.as_view(), name='two-sum'),
    path('three-sum/', ThreeSumView.as_view(), name='three-sum'),
    path('longest-non-repeat-substring/', LongestNonRepeatingSubstringView.as_view(), name="longest-non-repeat-substr"),
    path('longest_palindrome/', LongestPalindromeView.as_view(), name="longest_palindrome"),
    path('longest_increasing_subsequence/', LongestIncreasingSubsequence.as_view(), name="longest_increasing_subsequence"),
    path('valid_parenthesis/', ValidParenthesis.as_view(), name="valid_parenthesis"),
    path('trapped_rainwater/', TrappedRainwater.as_view(), name="trapped_rainwater"),
    path('product_of_array_except_self/', ProductOfArrayExceptSelf.as_view(), name="product_of_array_except_self"),
    path('container_of_water/', ContainerOfWater.as_view(), name="container_of_water")
]
