from django.urls import path

from .views import (
    ContainerOfWaterView,
    GroupAnagramsView,
    IsAnagramView,
    LongestIncreasingSubsequenceView,
    LongestNonRepeatingSubstringView,
    LongestPalindromeView,
    MergeIntervalsView,
    ProductOfArrayExceptSelfView,
    ThreeSumView,
    TrappedRainwaterView,
    TwoSumView,
    ValidParenthesisView,
    ProblemListView
)

urlpatterns = [
    path('container_of_water/', ContainerOfWaterView.as_view(), name="container_of_water"),
    path('is_anagram/', IsAnagramView.as_view(), name="is_anagram"),
    path('longest_increasing_subsequence/', LongestIncreasingSubsequenceView.as_view(), name="longest_increasing_subsequence"),
    path('longest-non-repeat-substring/', LongestNonRepeatingSubstringView.as_view(), name="longest-non-repeat-substr"),
    path('longest_palindrome/', LongestPalindromeView.as_view(), name="longest_palindrome"),
    path('merge_intervals/', MergeIntervalsView.as_view(), name="merge_intervals"),
    path('product_of_array_except_self/', ProductOfArrayExceptSelfView.as_view(), name="product_of_array_except_self"),
    path('three-sum/', ThreeSumView.as_view(), name='three-sum'),
    path('trapped_rainwater/', TrappedRainwaterView.as_view(), name="trapped_rainwater"),
    path('two-sum/', TwoSumView.as_view(), name='two-sum'),
    path('valid_parenthesis/', ValidParenthesisView.as_view(), name="valid_parenthesis"),
    path('group_anagrams/', GroupAnagramsView.as_view(), name="group_anagrams"),
    path('problems/', ProblemListView.as_view(), name="problems")
]
