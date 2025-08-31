# Leetcode 1
# Two sum done using arrays
# Time Complexity: O(N^2)
# Space Complexity: O(1)

def two_sum(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


print(two_sum([2, 7, 11, 15], 9))

# Leetcode Style with class

# Typing module allows developers to specify the expected data types of variables, function parameters,
# and return values

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]   # return as soon as found
        return []  # if no solution (though problem guarantees one)

sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

# ✅ Edge Cases for Two Sum
#
# Empty array
# nums = [], target = 5
# No numbers to add.
#
# Single element array
# nums = [3], target = 3
# Not enough numbers to form a pair.
#
# No valid pair exists
# nums = [1, 2, 3, 4], target = 100
# Nothing sums to target.
#
# Pair is the same number used twice
# nums = [2, 2, 3], target = 4
# Must return the indices of the two different 2s.
#
# Target is zero
# nums = [0, 4, 3, 0], target = 0
# Must handle zeros correctly ([0, 3]).
#
# Negative numbers included
# nums = [-3, 4, 3, 90], target = 0
# Solution is [-3, 3].
#
# Multiple valid pairs
# nums = [3, 3, 4, 5], target = 6
# Multiple answers possible — implementation should consistently return the first found.
#
# Large input size
# nums with ~10⁵ elements
# Tests performance; brute force (O(n²)) may time out, but optimized (O(n)) works.