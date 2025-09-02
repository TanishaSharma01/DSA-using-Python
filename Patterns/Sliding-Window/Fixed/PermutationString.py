# Leetcode 567
# Similar to Leetcode 438

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        n = len(s2)

        if k > n:
            return False

        s1_freq = {}
        s2_freq = {}

        for i in range(0, k):
            s1_freq[s1[i]] = s1_freq.get(s1[i], 0) + 1
            s2_freq[s2[i]] = s2_freq.get(s2[i], 0) + 1

        if s1_freq == s2_freq:
            return True

        l = 0
        for r in range(k, n):
            s2_freq[s2[r]] = s2_freq.get(s2[r], 0) + 1
            s2_freq[s2[l]] -= 1

            if s2_freq[s2[l]] <= 0:
                s2_freq.pop(s2[l])

            l += 1

            if s2_freq == s1_freq:
                return True

        return False

sol = Solution()
print(sol.checkInclusion("bac", "dfhhdhhdacbsms"))
print(sol.checkInclusion("bac", "dnddbd"))