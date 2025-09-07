# Leetcode 215 Medium

import heapq
from typing import List
# solved using min heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # create a heap of first k elements
        heap = nums[:k]
        heapq.heapify(heap)

        # process the rest of the elements
        for x in nums[k:]:
            if x > heap[0]:
                heapq.heapreplace(heap, x)

        # sort in descending order
        heap = sorted(heap, reverse=True)

        # return the element at k-1 index or the last element
        return heap[-1]  # or heap[k-1]
