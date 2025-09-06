#Leetcode 797 Medium
from typing import List

# Time: O(#paths × avg path length), Space: O(n) recursion stack + path storage
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        #dfs
        def dfs(graph, u, target, result, temp):
            temp.append(u)
            # if we reach the target append it to temp
            if u==target:
                #temp[:] to append a copy of the current path,
                #so backtracking doesn’t mutate the already stored paths
                result.append(temp[:])
            # ekse perform dfs
            else:
                for v in graph[u]:
                    dfs(graph, v, target, result, temp)
            temp.pop()

        n = len(graph)

        source = 0
        target = n-1

        result = []
        temp = []

        dfs(graph, source, target, result, temp)

        return result
