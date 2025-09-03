# Leetcode 11 Medium

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # area of container is height of shorter line between the two multiplied by
        # the distance between the two lines
        # area = min(height[left], height[right]) * (right-left)
        # the idea is we start with the widest possible area then move the pointer pointing
        # at shorter height inwards

        # left pointer at the beginning
        left = 0
        # right pointer at the end
        right = len(height) - 1
        # max area possible
        maxArea = 0
        # current area
        currentArea = 0

        # do this until left pointer smaller than equal to right
        while left <= right:
            # current area of the container updated
            currentArea = min(height[left], height[right]) * (right - left)
            # max area of the container
            maxArea = max(currentArea, maxArea)
            # compare heights
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxArea



