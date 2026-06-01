# Leetcode 283 Easy
# Time Complexity O(n), Space Complexity O(1)
from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # right pointer to find the location of non-zero element and left pointer
        # to track the position of zero you want to swap your non zero element with

        # left to track zero positions
        left = 0

        # right to track non zero positions
        for right in range(0, len(nums)):
            # if right finds non zero
            if nums[right] != 0:
                # swap elements
                temp = nums[left]
                nums[left] = nums[right]
                nums[right] = temp
                left += 1
