# Leetcode 57 medium
# Time complexity O(n)

from typing import List
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []

        for i in range(len(intervals)):
            # new = (2,5), i = (7,9), so basically the new interval tb inserted would lie
            # before this particular interval
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] # rest as it is
            # newInterval lies after this particular interval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # merging intervals
            else:
                # update new interval
                newInterval = [min(newInterval[0], intervals[i][0]),max(newInterval[1], intervals[i][1])]
        # append new Interval incase the if statement doesnt execute
        res.append(newInterval)
        return res

