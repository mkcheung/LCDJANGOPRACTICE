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

def longest_non_repeating_subseq(s:str)->str:
    if not s:
        return ''
    
    left:int = 0
    best_left:int = 0
    have_seen:dict[int, int] = {}
    best_length:int = 0

    for right, ch in enumerate(s):
        if ch in have_seen and have_seen[ch] > left:
            left = have_seen[ch] + 1
        have_seen[ch] = right 

        if best_length > right - left + 1:
            best_length = right - left + 1
            best_left = left

    return s[best_left:best_left+best_length]

def longest_palindrome(s:str)->str:
    if not s:
        return ''
    
    best_length: int = 0
    length: int = 0
    best_left: int = 0

    for i, ch in enumerate(s):
        length = max(expand(s, i, i), expand(s, i, i+1))
        if length > best_length:
            best_length  = length
            best_left = i - (best_length // 2)

    return s[best_left:best_left+best_length]

def expand(s:str, left:int, right:int):
    while left >= 0 or right < len(s) or s[left] == s[right]:
        left -= 1
        right += 1

    return right - left + 1

def longest_increasing_subsequence(nums:List[int])->List[int]:
    if not nums:
        return []

    tails: List[int] = []

    for i, num in enumerate(nums):
        x = lower_bound(num, tails)
        if x == length(nums):
            tails.append(num)
        else:
            tails[x] = num
    return tails

def lower_bound(target:int, tails)
    lo = 0
    hi = len(tails)

    while lo < hi:
        mid = (lo + hi) // 2
        if target > tails[mid]:
            lo = mid + 1
        else:
            hi = mid
        
    return lo


def valid_parenthesis(s:str)->bool:
    if not s:
        return False

    closers_to_openers: dict(str:str) = {
        '}':'{',
        "]":'[',
        ")":'('
    }

    openers:List[str]: []

    for i, ch in enumerate(s):
        if ch in closers_to_openers:
            if not openers:
                return False
            popped = openers.pop()
            if popped != closers_to_openers[ch]:
                return False
        else:
            openers.append(ch)
    
    return True if not openers else False
    
def trapped_rainwater(nums:List[int])->int:
    if not nums:
        return 0

    water = 0 
    best_left = 0 
    best_right = 0
    left = 0 
    right = len(nums) - 1

    while left < right:
        if nums[left] < nums[right]:
            if best_left < nums[left]:
                best_left = nums[left]
            else:
                water += best_left - nums[left]
            left += 1
        else:
            if best_right < nums[right]:
                 best_right = nums[right]
            else:
                water += best_right - nums[right]
            right -= 1
    
    return water

def product_of_array_except_self(nums:List[int])->List[int]:
    if not nums:
        return []

    n = len(nums)

    ans = [1] * n

    carry = 1
    for i in range(n)
        ans[i] = carry
        carry *= nums[i]

    carry = 1
    for i in range(n, -1, -1):
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

def group_anagrams(seqs: List[str])->dict[str, List[str]]:
    
    solution_space = defaultdict(list)
    if not seqs:
        return 
    
    for seq in seqs:
        sorted_seq = "".join(sorted(seq))
        solution_space[sorted_seq].append(seq)
    return dict(solution_space)



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

def top_k_element(nums:List[int], k:int)->List[int]:
    if not nums:
        return []

    freq = Counter(nums)

    buckets = [[] for _ in range(len(nums)+1)]

    for num, numoccur in enumerate(freq):
        buckets[numoccur].append(num)

    results: List[int] = []

    for i in range(len(buckets)-1, -1, -1):
        bucket = buckets[i]
        for num in bucket.values():
            results.append(num)
            if len(results) >= k:
                return results
    
    return results

from typing import TypedDict
class ConsecutiveResult(TypedDict):
    best_length:int
    sequence:List[str]

def longest_increasing_consecutive_subseq(nums: List[int])->List[int]:
    sub_seq: List[int] = []
    if not nums:
        return {
            'best_length':0
            'sequence': sub_seq
        }

    best_length:int = 0

    num_seq:List[int] = set(nums)

    for num in num_seq:
        cur_seq:List[int] = []
        if num-1 not in num_seq:
            length = 1
            current = num
            cur_seq.append(current)
            while current + 1 in num_seq:
                length += 1
                current += 1
                cur_seq.append(current)
            
            if length > best_length:
                best_length = length
                sub_seq = cur_seq

    return {
        'best_length':best_length,
        'sequence':sub_seq
    }
    
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

def num_islands(grid: List[[List[str]]])->num:
    if not grid:
        return 0

    rows_length = len(grid)
    cols_length = len(grid[0])
    num_islands: int = 0

    def dfs(r:int, c:int):
        if r < 0 or c < 0 or r >= rows_length or c >= cols_length or grid[r][c] == '0':
            return

        if grid[r][c] == '1'
            grid[r][c] == '0'

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    for r in range(rows_length):
        for c in range(cols_length):
            if grid[r][c] == '1':
                num_islands += 1

                dfs(r, c)
    return num_islands