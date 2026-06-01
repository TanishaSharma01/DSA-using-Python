# Leetcode 56 Medium

# O(n log n)
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # sort by starting values of intervals
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]  # for an edge case

        # keep note of start and end of the current interval
        for start, end in intervals[1:]:
            # most recently added interval's end value
            lastEnd = output[-1][1]
            # (1,5) (3,8) => (1,8)
            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            # (1,4) (6,8)
            else:
                output.append([start, end])

        return output



