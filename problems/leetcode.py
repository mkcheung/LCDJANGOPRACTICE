def three_zeroes(nums: List[int]) -> List[List[int]]:
    solution_space: List[List[int]] = []
    if nums is None:
        return solution_space

    nums.sort()
    overall_length = len(nums)

    for i in range(overall_length - 2):
        
        if nums[i] > 0:
            break
        
        if i > 0 and nums[i] == nums[i+1]:
            continue

        left, right = i + 1, overall_length - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum == 0:
                solution_space.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
    
    return solution_space

def two_sum(nums:List[int], target:int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]
        else:
            seen[num] = i

    return []