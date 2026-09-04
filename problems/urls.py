from django.urls import path

from .views import TwoSumView, ThreeSumView, LongestNonRepeatingSubstringView, LongestPalindromeView

urlpatterns = [
    path('two-sum/', TwoSumView.as_view(), name='two-sum'),
    path('three-sum/', ThreeSumView.as_view(), name='three-sum'),
    path('longest-non-repeat-substring/', LongestNonRepeatingSubstringView.as_view(), name="longest-non-repeat-substr"),
    path('longest_palindrome/', LongestPalindromeView.as_view(), name="longest_palindrome")
]
