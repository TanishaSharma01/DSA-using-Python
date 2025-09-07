# To get the K largest elements from an array
# we will use min heap for this approach

# Time complexity O(n log k)
# Space Complexity O(k)

from typing import List
import heapq

class Solution:
    def KLargest(self, nums: List[int], k: int) -> List[int]:
        # empty list
        if k<=0:
            return []
        # return all elements sorted
        if k>=len(nums):
            return sorted(nums, reverse=True)

        # create a heap of first k elements of array
        heap = nums[:k]
        heapq.heapify(heap)

        # process the rest of the elements
        for x in nums[k:]:
            if x>heap[0]: # heap[0] is current smallest of top-k
                heapq.heapreplace(heap, x) # pop + push in O(log k)

        # heap contains the k largest in arbitrary heap order
        return sorted(heap, reverse=True) # sort if you want descending output

    def k_largest(self, nums, k):
        return heapq.nlargest(k, nums)


sol = Solution()
print(sol.k_largest([4,1,6,8,2,3], 2))
print(sol.KLargest([4,1,6,8,2,3], 2))