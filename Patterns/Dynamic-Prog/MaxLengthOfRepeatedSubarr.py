# Leetcode 718 Medium
# T: O(M*N)
# S: O(M*N)

from typing import List
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # nums2 →  X   3   2   1   4   7
        # nums1 ↓
        # X         0   0   0   0   0   0
        # 1         0   0   0   1   0   0
        # 2         0   0   1   0   0   0
        # 3         0   1   0   0   0   0
        # 2         0   0   2   0   0   0
        # 1         0   0   0   3   0   0

        # ==> Max = 3

        m, n = len(nums1), len(nums2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ans = 0

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                    ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = 0
        return ans