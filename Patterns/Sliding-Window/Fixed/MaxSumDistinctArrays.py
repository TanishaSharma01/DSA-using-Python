# Leetcode 2461

from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # length of nums array
        n = len(nums)

        # check if length of k greater than nums
        if k > n:
            return 0

        # create a dictionary to store frequency of subarray
        subarray = {}

        # window sum
        windowSum = 0

        # set frequency and windowSum
        for i in range(0, k):
            subarray[nums[i]] = subarray.get(nums[i], 0) + 1
            windowSum += nums[i]

        # if elements unique then update maxSum
        if len(subarray) == k:
            maxSum = windowSum
        else:
            maxSum = 0

        # for rest of te elements
        for j in range(k, n):
            # remove first element of window
            subarray[nums[j - k]] -= 1
            windowSum -= nums[j - k]
            # if frequncy 0, remove the element
            if subarray[nums[j - k]] == 0:
                subarray.pop(nums[j - k])

            # add new element to the right
            subarray[nums[j]] = subarray.get(nums[j], 0) + 1
            windowSum += nums[j]

            # update maxSum
            if len(subarray) == k:
                maxSum = max(maxSum, windowSum)

        return maxSum


