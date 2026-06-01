# Leetcode 200 Medium
from collections import deque
from typing import List

# Using DFS
# risk of hitting recursion limit if grid is huge
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # basically the idea is we perform a dfs whenever land(1) is found and convert it to water
        # and its adjacent land as well and increase the number of islands and then move on to
        # find the next time we find land again
        # time complexity O(mxn)
        # space complexity O(mxn)

        # number of islands we wish to return
        num_islands = 0
        # rows and cols values set
        rows, cols = len(grid), len(grid[0])

        # dfs at position i,j
        def dfs(i, j):
            # conditions where we ignore
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != '1':
                return
            else:
                # set current position to 0
                grid[i][j] = '0'
                # do the same for neighbors
                # right
                dfs(i, j + 1)
                # down
                dfs(i + 1, j)
                # up
                dfs(i - 1, j)
                # left
                dfs(i, j - 1)

        # iterate through the grid
        for r in range(rows):
            for c in range(cols):
                # wherever it is land
                if grid[r][c] == '1':
                    # increment number of islands
                    num_islands += 1
                    # call dfs at given position
                    dfs(r, c)

        return num_islands

# Using BFS
# avoids recursion, safer for very large grids.
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        def bfs(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"  # mark as visited

            while queue:
                i, j = queue.popleft()
                for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                        grid[x][y] = "0"
                        queue.append((x, y))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    num_islands += 1
                    bfs(r, c)

        return num_islands
