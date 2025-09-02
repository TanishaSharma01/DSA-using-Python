# Leetcode 438
# Optimized approach got time complexity of O(n)
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # list for result
        resultSet = []

        # length of the two given strings s and p
        n = len(s)
        k = len(p)

        # if p greater then s then no anagram
        if k > n:
            return []

        # dictionaries for p and window
        p_freq = {}
        s_freq = {}

        # set p dictionary and initialize the window dictionary with first k elements
        for i in range(k):
            p_freq[p[i]] = p_freq.get(p[i], 0) + 1
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1

        # if the two got the same frequencies, append the start index to result list
        if p_freq == s_freq:
            res = [0]
        else:
            res = []

        # left pointer
        l = 0

        # right pointer for sliding window
        for r in range(k, n):
            # update frequency of the character at r pointer
            s_freq[s[r]] = s_freq.get(s[r], 0) + 1
            # reduce frequency of the character at l pointer
            s_freq[s[l]] -= 1

            # if the character's freq less than equal to 0, pop
            if s_freq[s[l]] <= 0:
                s_freq.pop(s[l])

            # increment left pointer
            l += 1

            # if the two got same frequency, append the start index to result list
            if p_freq == s_freq:
                res.append(l)

        return res

sol = Solution()
print(sol.findAnagrams("abcdcba", "bac"))