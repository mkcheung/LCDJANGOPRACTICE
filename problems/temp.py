def three_zeroes(nums: List[int]) -> List[List[int]]:
    solution_space: List[int] = []
    
    if not nums:
        return []

    overall_length = len(nums)
    nums.sort()

    for i in range(overall_length - 2):
        if nums[i] >= 0:
            return solution_space
        
        if i > 0 and nums[i] == nums[i-1]:
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

def longest_non_repeating_substring(seq: str) -> str:
    if not seq:
        return ''

    left: int = 0 
    best_left: int = 0
    best_length: int = 0
    have_seen: Dict[str, int] = {}

    for right, ch in enumerate(seq):
        if ch in have_seen and have_seen[ch] > left:
            left = have_seen[ch] + 1
        have_seen[ch] = right
        if right - left + 1 > best_length:
            best_length = right - left + 1
            best_left = left
        
    return seq[best_left:best_left+best_length]

def longest_palindrome(seq: str) -> str:
    if not seq:
        return ''
    
    best_length: int = 0
    best_left: int = 0
    tails: List[str] = []

    for i, ch in enumerate(seq):
        length = max(expand(seq, i, i), expand(seq, i, i + 1))
        if length > best_length:
            best_length = length
            best_left = i - (best_length // 2)

    return seq[best_left:best_left+best_length]

def expand(s:str, left:int, right:int) -> int:
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    
    return right - left + 1

def longest_increasing_subseq(seq:List[int]) -> List[int]:
    if not seq:
        return []

    tails: List[int] = []

    for num in seq:
        x = lower_bound(tails, num)
        if len(tails) == x:
            tails.append(num)
        else:
            tails[x] = num
    
    return tails

def lower_bound(tails: List[int], target: int):
    lo: int = 0
    hi: int = len(tails)


    while lo < hi:
        mid = (lo + hi) // 2
        if target > tails[lo]:
            lo = mid + 1
        else:
            hi = mid
    
    return lo

def valid_parenthesis(seq:str) -> bool:
    if seq is None:
        return False
    
    closers_to_openers = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    openers: List[str] = []

    for i, ch in enumerate(seq):
        if ch in closers_to_openers:
            if not openers:
                return False
            popped = openers.pop()
            if closers_to_openers[ch] != popped:
                return False
        else:
            openers.append(ch)
    
    return True

def trapped_rainwater(nums: List[int]) -> int:
    if not nums:
        return 0
    
    best_left: int = 0
    best_right: int = 0
    left:int = 0
    right: int = len(nums) - 1
    water: int = 0

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

    ans = [1] * n

    carry = 1

    for i in range(nums):
        ans[i] = carry
        carry *= nums[i]

    carry = 1 

    for i in range(len(nums) - 1, 0, -1):
        ans[i] *= carry
        carry *= nums[i]
    
    return ans

def container_of_water(nums: List[int]) -> int:
    if not nums:
        return 0
    
    left:int = 0
    right:int = len(nums) - 1
    best_water:int = 0

    while left < right:
        height = min(nums[left], nums[right])
        base = right - left
        water = height * base
        best_water = water if water > best_water else best_water
        if nums[left] < nums[right]:
            left += 1
        elif nums[right] < nums[left]:
            right -= 1
        else:
            right -= 1
        
    return best_water

from collections import defaultdict

def group_anagrams(seqs: List[str]) -> List[List[str]]:
    if not seqs:
        return False

    grouped = defaultdict(list);

    for i, seq in enumerate(seqs):
        sorted = "".join(sorted(seq))
        grouped[sorted].append(seq)

    return grouped

def merge_intervals(seqs: List[List[int]]) -> List[List[int]]:
    if not seqs:
        return []
    
    seqs = sorted(seqs, key = lambda s: (s[0], s[1]))

    merged = [seqs[0]]

    for start, end in seqs[1:]:
        latest = merged[-1]
        if latest[1] >= start:
            latest[1] = max(end, latest[1])
        else:
            merged.append([start, end])
    
    return merged

from collections import defaultdict

def is_anagram(seq1: str, seq2:str) -> bool:
    if not seq1 or not seq2 or len(seq1) != len(seq2):
        return False
    
    count = defaultdict(int)

    for i in range(len(seq1)):
        count[seq1[i]] += 1
        count[seq2[i]] -= 1

    return all( v == 0 for v in count.values())
    
from collections import Counter

def top_k_element(nums: List[int], num_elements: int) -> List[int]:
    if not nums or not num_elements:
        return []
    
    freq = Counter(nums)

    buckets = [ [] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    result: List[int] = []
    for i in range(len(buckets)-1, 0, -1):
        for num in buckets[i]:
            result.append(num)

        if len(result) >= num_elements:
            return result
    
    return result

from typing import TypedDict

class ConsecutiveResult(TypedDict):
    best_length: int
    sequence: List[str]

def longest_increasing_consecutive_subseq(nums:List[int]) -> ConsecutiveResult:
    if not nums:
        return {"Best Length": 0, "Sequence": []}

    num_seq = set(nums)
    best_length: int = 0 
    length: int = 0
    sub_seq: List[int] = []

    for num in nums:
        cur_seq = []
        if(num - 1 in num_seq):
            length = 1
            current = num
            cur_seq.append(current)
            while(current + 1 in num_seq)
                length += 1
                current += 1
                cur_seq.append(current)

            if length > best_length:
                best_length = length
                sub_seq = best_length
    
    return {
        'best_length': best_length,
        'sequence': sub_seq
    }

import heapq

def kth_largest_element(nums:List[int], k:int):
    heap: list = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heapq) >= k:
            heapq.heappop(heap)

    return heap[0]

grid1 = [
    ['1', '1', '1', '1', '0'],
    ['1', '1', '0', '1', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '0', '0', '0'],
]  # only 1 island here

grid2 = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1'],
]  # only 3 islands here

def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    count = 0 

    def dfs(r:int, c:int):
        if r < 0 or c < 0 or r >= rows or c >= col or grid[r][c] == '0':
            return
        grid[r][c] = '0'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if(grid[r][c] == 1):
                count += 1
                dfs(r, c)