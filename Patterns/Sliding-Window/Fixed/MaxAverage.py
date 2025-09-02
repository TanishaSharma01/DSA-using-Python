# Leetcode problem 643 Easy
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Brute force method uses a nested for loop to find the max sum, them divide by k to get the maximum average which has time complexity of O(n^2).

        # length of array
        n = len(nums)

        # calculating sum of first k elements
        sum = 0
        for i in range(0, k):
            sum += nums[i]

        # slide the window across the array
        maxSum = sum
        for j in range(k, n):
            sum -= nums[j - k]  # remove element leaving window
            sum += nums[j]  # add new element entering window
            maxSum = max(maxSum, sum)  # update max sum

        return maxSum / k

sol = Solution()
print(sol.findMaxAverage([2,6,7,8,10], 2))

