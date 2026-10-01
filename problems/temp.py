def three_zeroes(nums:List[int]) -> List[List[int]]:
    if not nums:
        return []

    solution_space: List[[List[int]]]

    nums = sort(nums)

    overall_length = len(nums)

    for i in range(overall_length - 2):
        if nums[i] >= 0:
            return solution_space

        if i > 0 and num[i] == num[i-1]:
            continue
        
        left, right = i + 1, overall_length - 1

        while left < right:
            thesum = nums[i] + nums[left] + nums[right]
            if thesum == 0:
                solution_space.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif thesum < 0:
                left += 1
            else:
                right -= 1
        
    return solution_space

def two_sum(nums:List[int], target:int) -> bool:
    if not nums:
        return []
    
    have_seen: Dict(int,int)

    for i, num in enumerate(nums):
        complement = target - num
        if complement in have_seen:
            return [have_seen[complement], i]
        else:
            have_seen[num] = i
    return[]

def longest_non_repeating_substring(seq: str) -> str:
    if not seq:
        return ''

    last_seen: Dict(str, int) = {}
    left: int = 0
    best_left: int = 0
    best_length: int = 0

    for right, ch in enumerate(seq):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        
        last_seen[ch] = right
        
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

def group_anagrams(seqs:List[str]) -> List[List[str]]:
    if not seqs:
        return []

    grouped = defaultdict(list)

    for seq in seqs:
        sorted = "".join(sorted(seq))
        grouped[sorted].append(seq)

    return grouped

def merge_intervals(seqs:List[List[int]]) -> List[int]:
    if not seqs:
        return []

    merged:List[List[int]] = [] 

    seqs = sorted(seqs, key = lambda s: (s[0], s[1]))

    merged[list(seqs[0])]

    for start, end in seqs[1:]:
        current = merged[-1]
        if current[1] >= start:
            current[1] = max(current[1], end)
        else:
            merged.append([start, end])

    return merged


from collections import defaultdict

def is_anagram(str1:str, str2:str) -> bool:
    if not str1 or not str2 or len(str1) != len(str2):
        return False

    count = defaultdict(int)

    for i in range(len(str1)):
        count[str1[i]] += 1
        count[str2[i]] -= 1
    
    return all( v == 0 for v in counts.values())

from collections import Counter

def top_k_element(nums:List[int], k:int) -> List:int:
    if not nums:
        return [] 

    freq = Counter(nums)

    buckets = [ [] for _ in range(len(nums) + 1) ]
    for numoccur, num in freq.items():
        buckets[numoccur].append(num)
    
    result: List[int] = []

    for i in range(len(buckets)-1, 0, -1):
        for num in bucket[i]:
            result.append(num)

            if len(result) = k
                return result
    
    return result


from typing import TypedDict

class ConsecutiveResult(TypedDict):
    best_length: int
    sequence: List[int]

def longest_increasing_consecutive_subseq(seq: List[int]) -> List[int]:
    sub_seq: List[int] = []

    if not seq:
        return {
            'best_length':0,
            'sequence':[]
        }

    num_set: List[int] = set(seq)
    best_length: int = 0

    for num in nums:
        cur_seq:int = List[]
        if num - 1 in num_set:
            length = 1
            current = num
            cur_seq.append(num)
            while current + 1 in num_set:
                length += 1
                current += 1
                cur_seq.append(current)
            if length > best_length:
                best_length = length
                sub_seq = cur_seq

    return sub_seq



import heapq

def kth_largest_element(nums: List[int], k:int) -> int:
    heap = []

    for i, num in enumerate(nums):
        heapq.heappush(heap, num)
        if len(heap) > k:
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
    
    rows:int = len(grid)
    cols:int = len(grid[0])
    num_islands: int = 0

    def dfs(r:int, c:int):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0'
            return
        
        grid[r][c] = '0'

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1'
                num_islands += 1
                dfs(r, c)

    return num_islands