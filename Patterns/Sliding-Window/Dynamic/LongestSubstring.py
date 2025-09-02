# Leetcode problem 3 Medium

# Brute force method involves checking every substring and checking if it has repeating characters
# and if not then storing the length.
# Time Complexity of this approach is O(N^3)
# Optimized approach uses Dynamic Sliding Window (where window length is not fixed)
# Time Complexity O(N)
# Space Complexity O(k) where k is the length of character set, in worst case it is O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)
        seen = set()
        left = 0
        maxLength = 0

        for right in range(0, n):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            maxLength = max(maxLength, right - left + 1)

        return maxLength


sol = Solution()
print(sol.lengthOfLongestSubstring("abcde"))
print(sol.lengthOfLongestSubstring("abacus"))
print(sol.lengthOfLongestSubstring("kewkew"))