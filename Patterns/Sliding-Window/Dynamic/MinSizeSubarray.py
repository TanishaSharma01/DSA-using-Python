# Leetcode 209 Medium
from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # size of nums array
        n = len(nums)
        # result minimum length
        min_len = 1000000000
        # sum of window
        sum = 0
        # right pointer
        right = 0
        # length of current window
        window_len = 0

        for left in range(0, n):
            # condition
            while sum < target:
                # index out of bounds
                if right < n:
                    # right element added
                    sum += nums[right]
                    right += 1
                else:
                    if min_len == 1000000000:
                        return 0
                    else:
                        return min_len
            # window length updated
            window_len = right - left
            # minimum length updated
            min_len = min(window_len, min_len)
            # left element deleted
            sum -= nums[left]

        return min_len



