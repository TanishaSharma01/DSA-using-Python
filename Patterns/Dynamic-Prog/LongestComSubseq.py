# Leetcode 1143 Medium
# T: O(m*n)
# S: O(m*n)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
            #    X  a  b  c  d  e
            #     +-------------------
            # X |  0  0  0  0  0  0
            # a |  0  1  1  1  1  1
            # c |  0  1  1  2  2  2
            # e |  0  1  1  2  2  3


        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        text1 = list(text1)
        text2 = list(text2)

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]

