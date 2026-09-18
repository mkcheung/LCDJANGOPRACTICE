def three_zeroes(nums: List[int]) -> List[List[int]]:
    solution_space: List[int] = []
    
    if not nums:
        return []

    overall_length = len(nums)
    nums.sort()

    for i in range(overall_length - 2):
        if nums[i] >= 0:
            return solution_space
        
        if i > 0 and nums[i] == nums[i-1]
            continue

        left, right = i + 1, overall_length - 1

        while left < right:
            sum = nums[i] + nums[left] + nums[right]

            if sum == 0:
                solution_space.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1

                while left < right and nums[right] == right[right-1]:
                    right -= 1

                left += 1
                right -= 1
            elif sum < 0:
                left += 1
            else:
                right -= 1
        
    return solution_space

def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}

    if not nums:
        return []

    for i, num in enumerate(nums):
        complement = num - target
        if complement in seen:
            return [seen[complement], i]
        else:
            seen[num] = i
    
    return []

def longest_non_repeating_substring(s:str) => str:
    if not s:
        return ''

    best_len, best_left = 0, 0
    last_seen = {}
    left = 0

    for right, ch in enumerate(s):
        if ch in last_seen:
            left = last_seen[ch] + 1
        last_seen[ch] = right

        if right - left + 1 > best_len:
            best_len = right - left + 1
            best_left = left
    
    return s[best_left:best_left+best_len]

def longest_palindrome(s:str) -> str:
    if not s:
        return ''
    
    best_length: int = 0
    best_left: int = 0

    for i in range(len(s)):
        length = max(expand(s, i, i), expand(s, i, i+1))
        if length > best_length:
            best_length = length:
            best_left = i - (best_length // 2)
    
    return s[best_left:best_left + best_length]

def expand(s:str, left: int, right: int):
    while left >= 0 and right < len(right) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return right - left - 1

def longest_increasing_subseq(nums: List[int]) -> List[int]:
    if not nums:
        return [] 

    tails: List[int] = []

    for i, num in enumerate(nums):
        x: int = lower_bound(tails, num)
        if x == len(tails):
            tails.append(x)
        else:
            tails[x] = num
        
    return tails

def lower_bound(tails: List[int], target:int) -> int:
    lo = 0
    hi = len(tail)

    while lo < hi:
        mid = (lo + hi) // 2
        if tails[mid] < target:
            lo = mid + 1 
        else
            hi = mid
    
    return lo

def valid_parenthesis(s:str) -> return bool:
    if not s:
        return False

    openers: List[str]: []

    closers_to_openers = {
        ')':'('
        '}':'{'
        ']':'['
    }

    for i, ch in enumerate(s):
        if ch in closers_to_openers:
            if not openers:
                return False
            popped = openers.pop()
            if closers_to_openers[ch] != popped
                return False
        else:
            openers.append(ch)

    return True if not openers else False

def trapped_rainwater(nums: List[int]) -> int:
    if not nums:
        return 0

    water = 0 
    best_left = 0
    best_right = 0
    left = 0
    right = len(nums)-1

    while left < right:
        if nums[left] < nums[right]:
            if nums[left] > best_left:
                best_left = nums[left]
            else:
                water += best_left - nums[left]
            left += 1
        else:
            if nums[right] > best_right:
                best_right = nums[right]
            else:
                water += best_right - nums[right]
            right -= 1
    
    return water
                
def product_of_array_except_self(nums: List[int]) -> List[int]:
    if not nums:
        return []
    
    length = len(nums)
    ans = [1] * length

    carry: int = 1

    for i in range(nums):
        ans[i] = carry
        carry *= nums[i]

    carry = 1
    for i in range(len(nums)-1, 0, -1):
        ans[i] *= carry
        carry *= nums[i]
    
    return ans

def container_of_water(heights: List[int]) -> int:
    if not heights:
        return 0

    best_water:int = 0
    water:int = 0
    left: int = 0 
    right: int = len(heights)-1

    while left < right:
        height = max(heights[left], heights[right])
        base = right - left
        water = height * base
        if water > best_water:
            best_water = water
        
        if heights[left] > heights[right]:
            left += 1
        elif heights[right] > heights[left]:
            right -= 1
        else:
            right -= 1
    
    return best_water

from collections import defaultdict

def group_anagrams(s:List[str]) -> List[List[str]]:
    if not s:
        return []

    grouped = defaultdict(list)

    for i, term in enumerate(s):
        sorted_term = "".join(sorted(term))
        grouped[sorted_term].append(term)

    return grouped

def merge_intervals(seqs: List[List[int]]) -> List[List[int]]:
    if not seqs:
        return []

    seqs = sorted(seqs, key = lambda s:(s[0], s[1]))

    merged = [list(seqs[1])]

    for start, end in seqs[1:]:
        current = merged[-1]

        if current[1] <= start:
            current[1] = max(current[1], end)
        else:
            merged.append(start,end)
    
    return merged

from collections import defaultdict

def is_anagram(str1: str, str2: str) -> bool:
    if not str1 or not str2 or len(str1) != len(str2):
        return False

    counts = defaultdict(int)

    for i in range(len(str1)):
        counts[str1[i]]+=1
        counts[str2[i]]-=1

    return all( value == 0 for value in counts.values() )

from collections import Counter

def top_k_element(nums: List[int], num_elements: int) -> List[int]:
    if not nums or num_elements == 0:
        return False
    
    freq = Counter(nums)

    buckets = [for _ in range(len(nums)+1)]

    for num, count in freq.items():
        buckets[count].append(num)

    result = []

    for i in range(len(buckets)-1, 0, -1):
        for num in buckets[i]:
            result.append(num)

        if len(result == num_elements):
            return result
    return result

from typing import TypedDict

class ConsecutiveResult(TypedDict):
    'best_length': int
    'sequence': List[str]

def longest_consecutive_increasing_subseq(seqs:List[int]) -> ConsecutiveResult:
    if not seqs:
        return {
            'best_length': 0
            'sequence': []
        }

    sub_seq: List[int]
    length = 0
    best_length = 0

    num_seq = set(seqs)

    for num in num_seq:
        cur_seq = []
        if num - 1 not in num_seq:
            length = 1
            current = num
            cur_seq.append(num)
            while current + 1 in num_seq:
                length += 1
                current += 1
                cur_seq.append(current)
            
            if length > best_length:
                best_length = length
                sub_seq = cur_seq
    
    return {
        'best_length': best_length
        'sequence': sub_seq
    }


import heapq

def kth_largest_element(nums: List[int], k: int) -> int | None:
    heap = []

    for num in nums: 
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap