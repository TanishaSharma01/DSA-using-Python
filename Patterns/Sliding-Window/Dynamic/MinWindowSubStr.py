# Leetcode 76 Hard

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        k = len(t)
        s_freq = {}
        t_freq = {}
        sub_string = s[0:k] if k <= n else ""  # Handle edge case

        if k > n:
            return ""

        # Helper function to check if current window contains all required chars
        def contains_all():
            for char, count in t_freq.items():
                if s_freq.get(char, 0) < count:
                    return False
            return True

        for i in range(0, k):
            s_freq[s[i]] = s_freq.get(s[i], 0) + 1
            t_freq[t[i]] = t_freq.get(t[i], 0) + 1

        min_window = sub_string if contains_all() else ""  # Track minimum window
        min_len = len(min_window) if min_window else float('inf')

        right = k
        for left in range(0, n - k + 1):  # Fix range
            while right < n and not contains_all():  # Fix condition + bounds check
                s_freq[s[right]] = s_freq.get(s[right], 0) + 1
                sub_string += s[right]
                right += 1

            # Check if current window is valid and smaller
            if contains_all() and len(sub_string) < min_len:
                min_window = sub_string
                min_len = len(sub_string)

            # Slide window: remove leftmost character
            if left + 1 < n:
                s_freq[s[left]] -= 1
                if s_freq[s[left]] == 0:
                    del s_freq[s[left]]
                sub_string = sub_string[1:]  # Remove first character

        return min_window