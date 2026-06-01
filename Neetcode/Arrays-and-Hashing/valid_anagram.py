# NEETCODE 150
# https://neetcode.io/problems/is-anagram/question

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for letter in s:
            if letter in dict1:
                dict1[letter] = dict1.get(letter) + 1
            else:
                dict1[letter] = 1

        for letter in t:
            if letter in dict2:
                dict2[letter] = dict2.get(letter) + 1
            else:
                dict2[letter] = 1

        if dict1 == dict2:
            return True
        return False