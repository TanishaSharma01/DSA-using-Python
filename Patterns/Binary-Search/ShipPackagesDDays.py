# Leetcode 1011 Medium
from typing import List

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # lower bound is the biggest weight that can be loaded
        lower = max(weights)
        # upper bound is sum of all weights
        upper = sum(weights)
        # initialize result to greatest value possible
        res = upper

        # function to check if given capacity would work with the days
        def canShip(cap):
            # initialize to 1
            ships = 1
            currCap = cap
            # iterate through all the weights
            for w in weights:
                # if currCap becomes less than 0, time to get a new ship
                if currCap - w < 0:
                    ships += 1
                    # reset currCap
                    currCap = cap
                # load weight
                currCap -= w
            # true or false
            return ships <= days

        while lower <= upper:
            cap = (lower + upper) // 2
            if canShip(cap):
                # result is stores as the minimum value
                res = min(res, cap)
                upper = cap - 1
            else:
                lower = cap + 1

        return res


