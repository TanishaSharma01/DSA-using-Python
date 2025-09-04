# Leetcode 42 Hard

from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        left_arr = [0] * len(height)
        right_arr = [0] * len(height)
        total = 0

        # left values incremented
        for i in range(0, len(height)):
            max_left = max(max_left, height[i])
            left_arr[i] = max_left

        # right values incremented
        for i in range(len(height) - 1, -1, -1):
            max_right = max(max_right, height[i])
            right_arr[i] = max_right

        for j in range(0, len(height)):
            total += min(left_arr[j], right_arr[j]) - height[j]

        return total



