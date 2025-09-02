# Leetcode 424 Medium

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # length of string
        s_len = len(s)
        # character frequency in window
        window_freq = {}
        # left pointer
        left = 0
        # maximum length, the result we'll be returning
        max_len = 0

        # right pointer
        for right in range(0, len(s)):
            # adding right element to the window frequency
            window_freq[s[right]] = window_freq.get(s[right], 0) + 1

            # get max frequency
            if window_freq:
                max_freq = max(window_freq.values())
            else:
                max_freq = 0

            # window length
            window_len = right - left + 1

            # shrink until condition satisfies, that is removing left elements
            while window_len - max_freq > k:
                window_freq[s[left]] -= 1

                if window_freq[s[left]] == 0:
                    window_freq.pop(s[left])
                # update left
                left += 1
                # window length updated
                window_len = right - left + 1
                # get the new max freq value
                if window_freq:
                    max_freq = max(window_freq.values())
                else:
                    max_freq = 0

            # update max length to return if necessary
            max_len = max(max_len, window_len)

        return max_len


