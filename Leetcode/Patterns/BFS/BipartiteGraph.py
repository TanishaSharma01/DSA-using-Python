# Leetcode 785 Medium
from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        odd = [0] * len(graph) # map node i -> odd = 1, even = -1

        def bfs(i):
            # already visited so traversal completed, exit
            if odd[i]:
                return True

            q = deque([i])
            odd[i] = -1  # mark even
            while q:
                i = q.popleft()
                for nei in graph[i]:
                    if odd[i] == odd[nei]:
                        return False
                    elif not odd[nei]:
                        q.append(nei)
                        odd[nei] = -1 * odd[i] # alternate marking
            return True

        # the graph might not be fully connected so bfs on all elements
        for i in range(len(graph)):
            if not bfs(i):
                return False
        return True

