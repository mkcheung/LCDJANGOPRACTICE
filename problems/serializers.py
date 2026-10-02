from rest_framework import serializers
from .leetcode import two_sum,three_zeroes,longest_non_repeating_substring, longest_palindrome, longest_increasing_subseq, valid_parenthesis, trapped_rainwater, product_of_array_except_self,container_of_water

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
        result = longest_non_repeating_substring(s)

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
        result = longest_increasing_subseq(nums)

        return {
            'result': result
        }

class ValidParenthesisSerializer(serializers.Serializer):
    s = serializers.CharField(
        allow_blank=False,
        trim_whitespace=True
    )

    result = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        s = validated_data['s']
        result = valid_parenthesis(s)

        return {
            'result': result
        }

class TrappedRainwaterSerializer(serializers.Serializer):
    heights = serializers.ListField(
        child=serializers.IntegerField()
    )

    water = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        heights = validated_data['heights']
        water = trapped_rainwater(heights)

        return {
            'water': water
        }

class ProductOfArrayExceptSelfSerializer(serializers.Serializer):
    nums = serializers.ListField(
        child=serializers.IntegerField()
    )

    ans = serializers.ListField(
        child=serializers.IntegerField(),
        read_only=True
    )

    def create(self, validated_data):
        nums = validated_data['nums']
        ans = product_of_array_except_self(nums)

        return {
            'ans': ans
        }

class ContainerOfWaterSerializer(serializers.Serializer):
    nums = serializers.ListField(
        child=serializers.IntegerField()
    )

    best_water = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        nums = validated_data['nums']
        best_water = container_of_water(nums)

        return {
            'best_water':best_water
        }