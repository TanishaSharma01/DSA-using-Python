# Leetcode 347 Medium

from typing import List
class Solution:
    # we use bucket sort instead of heaps because this is most efficient with
    # time complexity O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap to keep count of elements
        count = {}
        # freq array with nums size + 1 because an element can have k freq at max
        freq = [[] for i in range(len(nums) + 1)]

        # count of elements
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        # populate freq array with the the freq as index and the element as the value
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # get the k most frequent elements
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                # if len of result hit k
                if len(res) == k:
                    return res

# Using heaps with Time Complexity O(k log n)
import heapq
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Dictionary of frequencies
        counts = defaultdict(int)
        for num in nums:
            counts[num] += 1

        # Min heap
        heap = []

        # iterate through the elements in count dictionary
        for key, val in counts.items():
            # count is key now whereas the elemnt is value
            heapq.heappush(heap, (val, key))
            # if len of heap exceeds that of k, pop the minimum element
            if len(heap) > k:
                heapq.heappop(heap)

        # return the k most frequent elements
        return [key for (val, key) in heap]




