from rest_framework import serializers
from .leetcode import two_sum,three_zeroes,longest_non_repeatingsubstring, longest_palindrome, longest_increasing_subsequence

class ThreeSumSerializer(serializers.Serializer):
    
    nums = serializers.ListField(
        child=serializers.IntegerField()
    )

    result = serializers.ListField(
        child=serializers.IntegerField(),
        read_only=True
    )

    def create(self, validated_data):
        nums = validated_data['nums']
        result = three_zeroes(nums)

        return {
            'nums':nums,
            'result':result
        }

class TwoSumSerializer(serializers.Serializer):
    nums = serializers.ListField(
        child=serializers.IntegerField()
    )

    target = serializers.IntegerField()

    result = serializers.ListField(
        child=serializers.IntegerField(),
        read_only=True
    )

    def create(self, validated_data):
        nums = validated_data['nums']
        target = validated_data['target']
        result = two_sum(nums, target)

        return {
            'nums':nums,
            'result': result
        }

class LongestNonRepeatingSubstringSerializer(serializers.Serializer):
    s = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True
    )

    result = serializers.CharField(read_only=True)

    def create(self, validated_data):
        s = validated_data['s']
        result = longest_non_repeatingsubstring(s)

        return {
            'result': result
        }

class LongestPalindromeSerializer(serializers.Serializer):
    s = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True
    )

    result = serializers.CharField(read_only=True)

    def create(self, validated_data):
        s = validated_data['s']
        result = longest_palindrome(s)

        return {
            'result': result
        }

class LongestIncreasingSubsequenceSerializer(serializers.Serializer):
    nums = serializers.ListField(
        child=serializers.IntegerField()
    )

    result = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        nums = validated_data['nums']
        result = longest_increasing_subsequence(nums)

        return {
            'result': result
        }
