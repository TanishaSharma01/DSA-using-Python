# Leetcode 30 Hard

# Time Complexity O(N)
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # length of the string given
        s_len = len(s)
        # size of words array
        words_len = len(words)

        # check is size of words array is 0
        if words_len == 0:
            return []

        # length of one word
        len_word = len(words[0])
        # set window_size
        k = len(words[0]) * words_len

        if k > s_len:
            return []

        result = []
        window_freq = {}
        words_freq = {}
        window = ""

        for word in words:
            words_freq[word] = words_freq.get(word, 0) + 1

        right = len_word
        for i in range(0, k, len_word):
            sub_string = s[i:right]
            window += sub_string
            window_freq[sub_string] = window_freq.get(sub_string, 0) + 1
            right += len_word

        if words_freq == window_freq:
            result.append(0)

        for j in range(k, s_len):
            window = window[1:]
            window += s[j]

            window_freq = {}
            for i in range(0, len(window), len_word):
                sub_string = window[i:i + len_word]  # Extract from window, not s
                window_freq[sub_string] = window_freq.get(sub_string, 0) + 1

            if words_freq == window_freq:
                result.append(j - k + 1)

        return result