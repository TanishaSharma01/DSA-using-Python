# Leetcode 79 Medium
from typing import List
# time complexity O(R * C * 4^L)
# space complexity O(L)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        # set to append visited positions
        visited = set()
        # to append result values
        result = []
        # convert word to word array
        char_word = list(word)
        # pointer for the character in word array we are at
        i = 0

        # perform dfs on a position with a character[i]
        def dfs(r, c, i):
            # reached ans
            if i == len(word):
                return True
            # out of bounds, answer not here, return false
            if (r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    (r, c) in visited):
                return False
            # this particular dfs failed, return False
            if board[r][c] != char_word[i]:
                return False
            # add to visited
            visited.add((r, c))
            # append the character to result
            result.append(board[r][c])

            # dfs at neighbors
            found = (dfs(r, c - 1, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1))

            # backtrack
            if not found:
                # from result pop out the latest value
                result.pop()
                # remove from visited set
                visited.remove((r, c))
            # if found, return true, else false
            return found

        # iterate through all elements of graph
        for row in range(rows):
            for col in range(cols):
                # if the particular element is same as the first character, perform dfs
                if board[row][col] == char_word[i]:
                    # if dfs returned True
                    if dfs(row, col, 0):
                        return True
        return False




