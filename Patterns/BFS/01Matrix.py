# Leetcode 542 Medium
# multi source bfs
from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        # set to infinity
        result = [[float('inf')] * cols for _ in range(rows)]
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    q.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = r + dr, c + dc
                if 0 <= row < rows and 0 <= col < cols:
                    # update to better values
                    if result[row][col] > result[r][c] + 1:
                        result[row][col] = result[r][c] + 1
                        q.append((row, col))

        return result
