# Let's say we have a long list of unsorted numbers (potentially millions), and we want to find the M largest numbers contained in it. 
# Implement a function find_largest(input, m) that will find and return the largest m values given an input array or file.
# If the input array is empty, return None (Python) or null.

from typing import List, Optional
from heapq import heappush, heappop

def find_largest(input, m):

    if not input:
        return None
    
    max_nums = [float('-inf')]

    for i in input:
        if i > max_nums[0]:
            if len(max_nums) >= m:
                heappop(max_nums)
            heappush(max_nums, i)
    return max_nums

print(find_largest([7, 5, 4, 2, 3], 3))