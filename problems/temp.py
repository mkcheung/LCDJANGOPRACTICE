def three_zeroes(nums: List[int]) -> List[List[int]]:
    solution_space: List[int] = []

    if nums is None:
        return []

    overall_length = len(nums)
    nums.sort()

    for i in range(overall_length - 2):
        if nums[i] >= 0:
            return solution_space
        
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, overall_length -1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum == 0:
                solution_space.append(nums[i],nums[left],nums[right])

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

def two_sum(nums: List[int], target:int) -> List[int]:
    seen = {}

    for i, num in enumerate(nums):
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[num] = i
    
    return []

def longest_increasing_subsequence(s:str)
    if s is None:
        return ''
    
    best_length: int = 0
    best_left: int = 0
    last_seen = {}
    left: int = 0

    for right, ch in enumerate(s):
        if ch in last_seen and left > 0:
            left = last_seen[ch] + 1

        if right - left + 1 > best_length:
            best_length = right - left + 1
            best_left = left

        last_seen[ch] = right

    return s:[best_left:best_left+best_length]

def longest_palindrome(s:str) -> str:
    if s is None:
        return ''

    overall_length = len(s)
    best_length: int = 0
    best_left: int = 0 

    for i in range(overall_length):
        length = max(expand(s, i, i), expand(s, i, i+1))
        if length > best_length:
            best_length = length
            best_left = i - (best_length // 2)
    
    return s:[best_left:best_left+best_length]


def expand(s:str, left: int, right: int):
    overall_length = len(s)
    while left >= 0 and right < overall_length and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1

def longest_increasing_subsequence(nums: List[int])
    tails: List[int] = []

    for i, num in enumerate(nums):
        x = lower_bound(target, num)
        if x == len(tails):
            tails.append(x)
        else:
            tails[x] = num
    
    return tails

def lower_bound(tails: List[int], target) -> int:
    lo = 0 
    hi = len(tails)

    while lo < mid:
        mid = (lo + hi) // 2
        if target > num[mid]:
            lo = mid + 1 
        else:
            hi = mid
    
    return lo

def valid_parenthesis(s:str) -> bool:

    closer_to_opener = {
        ')' => '(',
        '}' => '{',
        ']' => '['
    }

    openers = []

    for i, ch in enumerate(s):

        if ch in closer_to_opener:
            if not openers:
                return False
            popped = openers.pop()

            if popped != closer_to_opener[ch]:
                return False
        else:
            openers.append(ch)
    
    return True if not openers else False

def trapped_rainwater(heights: List[int]) -> int:
    if not heights:
        return 0

    left:int = 0
    best_left: int = 0
    right: int = len(heights)
    best_right: int = 0

    while left < right:
        if nums[left] < nums[right]:
            if nums[left] > best_left:
                best_left = left
            else:
                water += best_left - nums[left]
            left += 1
        else:
            if nums[right] > best_right:
                best_right = right
            else:
                water += best_right - nums[right]
            right -= 1

    return water
                
def product_of_array_except_self(nums: List[int]) -> int:
    if not nums:
        return 0
    
    length = len(nums)

    ans = [1] * length

    carry = 1

    for i in range(length):
        ans[i] = carry
        carry *= nums[i]
    
    carry = 1

    for i in range(length - 1, -1, -1):
        ans[i] *= carry
        carry *= nums[i]

    return ans

def container_of_water(nums: List[int]):
    if not nums:
        return 0
    
    left = 0 
    right = len(nums) - 1
    best_height = 0 
    water = 0
    best_water = 0 

    while left < right:
        base = right - left
        best_height = min(nums[left], nums[right])
        water = base * best_height
        if water > best_water:
            best_water = water

        if nums[left] < nums[right]:
            left += 1
        elif nums[right] > nums[left]:
            right -= 1
        else:
            right -= 1
        
    return best_water

from collections import defaultdict

def group_anagrams(s: List[str]) -> List[List[str]]:
    if not s:
        return []

    grouped = defaultdict(list)

    for i, term in enumerate(s):
        sorted_string = "".join(sorted(term))
        grouped[sorted_string].append(term)

    return grouped

def merge_intervals(seqs: List[List[int]]) -> List[List[int]]

    if not seqs:
        return []

    seqs = sorted(seqs, key = lambda: s (s[0], s[1]))
    
    merged = [seqs[0]]

    for start, end in seqs[1:]:
        current = merged[-1]

        if current[1] >= start:
            current[1] = max(end, current[1])
        else:
            merged.append(start, end)

    return merged    

