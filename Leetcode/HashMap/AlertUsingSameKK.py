# Leetcode 1604 Medium
from collections import defaultdict, deque
from typing import List

# T: O(n log n) due to sorting
# S: O(n)
class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        n = len(keyName)

        times = defaultdict(list)

        for i in range(n):
            name = keyName[i]
            time = keyTime[i]

            t = time.split(':')
            h = int(t[0])
            m = int(t[1])

            times[name].append(h * 60 + m)

        ans = []

        for name in times:
            # sort the times of a particular person
            time_list = sorted(times[name])

            # create a double ended queue
            queue = deque()

            # iterate over time
            for time in time_list:
                # add new time to queue
                queue.append(time)

                # if the first(or the oldest) element and current time difference greater
                # than 60, then pop
                # at a time we only want the times on the queue that are in 1 hour window
                while time - queue[0] > 60:
                    queue.popleft()

                # if more than 3 times in an hour window, append the name to ans and return
                if len(queue) >= 3:
                    ans.append(name)
                    break

        # return sorted by alphabetical order name ans
        return sorted(ans)

