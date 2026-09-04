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
        complement = target - nums[i]
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[num] = i
    return []

# GIVEN A STRING OF CHARACTERS, FIND THE LONGEST POSSIBLE
# SEQUENCE THAT DOESN'T HAVE A REPEATING CHARACTER
# Time Complexity: O(n)
def longest_non_repeatingsubstring(s: str):
    best_left: int = 0
    best_len: int = 0
    last_seen = {}
    left: int = 0

    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right

        if right - left + 1 > best_len:
            best_len = right - left + 1
            best_left = left

    return s[best_left:best_left+best_len]

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
    
    return s[best_left:best_left+best_length]

def expand(s:str, left: int, right:int):
    n = len(s)

    while left >= 0 and right < n and s[left] == s[right]:
        left -= 1
        right += 1
    
    return right - left - 1

def longest_increasing_subsequence(nums: List[int]) -> List[int]:
    tails: List[int] = []

    if not nums:
        return

    for i, num in enumerate(nums):
        x = lower_bound(tails, num)
        if x == len(nums):
            tails.append(num)
        else:
            tails[x] = num

    return len(tails)


def lower_bound(tails: List[int], target:int):
    lo = 0
    hi = len(tails)

    while lo < hi:
        mid = (lo + hi) // 2
        
        if tails[mid] > target:
            lo = mid + 1
        else:
            hi = mid
    
    return lo

def valid_parenthesis(s:str) -> bool:
    if s is None:
        return False

    closer_to_opener = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    openers = []

    for i, ch in enumerate(s):
        if ch in closer_to_opener:
            if not openers:
                return False

            item = openers.pop()

            if item != closer_to_opener[ch]:
                return False
        else:
            openers.append(ch)
    
    return True if not openers else False

def trapped_rainwater(heights: List[int]) -> int:
    if heights is None:
        return 0

    water = 0
    left, right = 0, len(heights) - 1
    best_left, best_right = 0, 0 

    while left < right:
        if nums[left] < nums[right]:
            if nums[left] > best_left:
                best_left = nums[left]
            else:
                water += best_left - nums[left]
            left+=1
        else:
            if nums[right] > best_right:
                best_right = nums[right]
            else:
                water += best_right - nums[right]
            right-=1
    
    return water

def product_of_array_except_self(nums: List[int]) -> int:
    if nums is None: 
        return 0

    n = len(nums)

    ans = [1] * n

    carry = 1
    for i in range(len(nums)):
        ans[i] = carry
        carry *= nums[i]
    
    carry = 1

    for i in range (n-1, -1, -1):
        ans[i] *= carry
        carry *= nums[i]

    return ans

def container_of_water(nums:List[int]) -> int:
    if nums is None:
        return 0
    
    left: int = 0 
    right: int = len(nums) - 1
    best_left: int = 0
    best_right: int = 0
    best_water: int = 0

    while left < right:
        best_height = max(nums[left], nums[right])
        base = right - left
        water = best_height * base
        if water > best_water:
            best_water = water
        
        if nums[left] < nums[right]:
            left += 1
        elif nums[right] < nums[left]:
            right -= 1
        else:
            right -= 1

    return best_water

from collections import defaultdict

def group_anagrams(s: List[str]) -> List[List[str]]:
    
    grouped = defaultdict(list)
    for i, term in enumerate(s):
        sorted_string = "".join(sorted(term))
        grouped[sorted_string].append(term)

    return grouped

def merge_intervals(seqs: List[List[int]]) -> List[List[int]]:
    if seqs is None:
        return []

    seqs = sorted(seqs, key = lambda s: (s[0], s[1]))

    merged = [list(seqs[0])]

    for start, end in seqs[1:]:
        current = merged[-1]

        if start <= current[1]:
            current[1] = max(current[1], end)
        else:
            merged.append(start, end)

    return merged

from collections import defaultdict

def is_anagram(str1: str, str2: str) -> bool:
    if not str1 or not str2 or len(str1) != len(str2):
        return False

    counts = defaultdict(int)

    for i in range(len(str1)):
        counts[str1[i]]+=1
        counts[str2[i]]-=1

    return all(v==0 for v in counts.values())

