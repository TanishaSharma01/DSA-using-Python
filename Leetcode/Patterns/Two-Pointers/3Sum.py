# Leetcode 15 medium
# Time Complexity is O(n log n) + O()
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # first we want to sort
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            # num is not the first element and it is same as the previous element
            # we skip
            if i > 0 and num == nums[i - 1]:
                continue

            # set l and r pointer
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]])
                    # update l pointer for next number to be considered
                    l += 1
                    # keep skipping same numbers
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return res

