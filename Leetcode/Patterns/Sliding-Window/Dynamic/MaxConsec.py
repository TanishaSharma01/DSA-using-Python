# Leetcode 1004
# Similar to Leetcode 424 Character Replacement

from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        window_freq = {}
        left = 0
        max_len = 0

        for right in range(0, n):
            window_freq[nums[right]] = window_freq.get(nums[right], 0) + 1

            zeros_count = window_freq.get(0, 0)

            window_len = right - left + 1
            while zeros_count > k:
                window_freq[nums[left]] -= 1

                if window_freq[nums[left]] == 0:
                    window_freq.pop(nums[left])

                left += 1

                window_len = right - left + 1

                zeros_count = window_freq.get(0, 0)

            max_len = max(max_len, window_len)

        return max_len  # Moved outside the loop