# Leetcode 452 Medium
from typing import List
# Time complexity O(n log n)
# Space Complexity O(log n)
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # if no points
        if not points:
            return 0

        points.sort()
        # we always need at least one arrow
        arrows = 1
        # prevEnd initialized to end of first interval
        prevEnd = points[0][1]

        for start, end in points[1:]:
            # if no overlap
            if start > prevEnd:
                arrows += 1
                prevEnd = end
            # if overlap, take the smaller end because that is one of the points we can shoot
            # arrow at
            else:
                prevEnd = min(prevEnd, end)
        return arrows