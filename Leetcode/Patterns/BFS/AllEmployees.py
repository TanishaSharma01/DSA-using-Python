# Leetcode 1376 Medium
from collections import deque
import collections
from typing import List


# Attempting DFS, time limit exceeded

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # we'll be using dfs

        def dfs(i):
            # maximum time to reach a subordinate
            max_time = 0
            # we'll iterate over all employees
            for j in range(n):
                # if an employee's manager is i
                if manager[j] == i:
                    # set that manager to -1
                    manager[j] = -1  # mark visited
                    # max of the max time and dfs of an employee
                    max_time = max(max_time, dfs(j))
            # a manager's inform time added with the max time
            return informTime[i] + max_time

        # performing dfs on head
        total = dfs(headID)
        # return total
        return total

# using bfs instead
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = collections.defaultdict(list)  # Mgr -> [list of emps]

        # create a dictionary with key as manager and values as employees
        for i in range(n):
            adj[manager[i]].append(i)

        print(adj)

        # BFS
        q = deque([(headID, 0)])  # creating a tuple (id, time)
        # to store result
        res = 0
        # while queue not empty
        while q:
            # store id and time where
            # time is  the total minutes it took for employee id to get the news
            id, time = q.popleft()
            # update result with whatever is bigger
            res = max(res, time)
            # for an employee for the popped id
            for emp in adj[id]:
                # time = when the manager got the news.
                # informTime[id] = how long they take to pass it down.
                # Their subordinate emp will only hear the news at time + informTime[id]
                q.append((emp, time + informTime[id]))
        return res



