# Leetcode 88 Easy but Medium level difficulty
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # we start from the biggest element that if from end
        # last index nums1
        last = m + n - 1

        # merge from reverse order
        while m > 0 and n > 0:
            # larger element of nums1 sent to the end
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            # nums 2 element larger
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        # fill nums1 with the leftover elements of nums2
        while n > 0:
            nums1[last] = nums2[n - 1]
            n -= 1
            last -= 1
