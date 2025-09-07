# Leetcode 435 Medium
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # O(n log n)
        # sort intervals
        intervals.sort()
        # store result
        res = 0
        # prev end initizalized to the end of first interval
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            # intervals dont overlap (1,3) (2,5) prevEnd = 3, start = 2, end = 5
            if start >= prevEnd:
                # update prevEnd
                prevEnd = end  # prevEnd = 5
            # Overlapping (1,3) (1,4) prevEnd = 3 (essentially we're removing (1,4) in a way)
            else:
                # incrementing count
                res += 1
                prevEnd = min(end, prevEnd)

        return res