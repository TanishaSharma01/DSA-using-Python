# Leetcode 242 Easy
from operator import truediv


# Solution without external libraries
# Time complexity O(n^2)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for l in set(s):
            if s.count(l) != t.count(l):
                return False
        return True


sol = Solution()
print(sol.isAnagram("alpha", "phala"))

from collections import Counter
class Solution2:
    def isAnagram2(self, s: str, t: str) -> bool:
        if Counter(s) == Counter(t):
            return True
        return False


sol2 = Solution2()
print(sol2.isAnagram2("alpha", "phala"))

