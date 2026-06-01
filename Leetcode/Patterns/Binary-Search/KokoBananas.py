# Leetcode 875 Medium

# time complexity O(n log m)
import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower = 1
        upper = max(piles)
        res = upper

        def canEat(cap):
            hours = 0
            for p in piles:
                # koko can take more than one hour to finish a pile
                hours += math.ceil(p / cap)
            return hours <= h

        while lower <= upper:
            cap = (upper + lower) // 2
            if canEat(cap):
                res = min(cap, res)
                upper = cap - 1
            else:
                lower = cap + 1

        return res