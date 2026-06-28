from rest_framework import serializers
from .leetcode import three_zeroes

class ThreeSumSerializer(serializers.Serializer):
    
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
        result = three_zeroes(nums)

        return {
            'nums':nums,
            'result':result
        }