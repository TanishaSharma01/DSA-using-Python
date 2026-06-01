# Leetcode 70 Easy

class Solution:
    def climbStairs(self, n: int) -> int:
        # for last stair we can only take 1 step (two)
        # for second last star we can only take 2 steps (one)
        one, two = 1, 1

        # basically fibonacci
        for i in range(n - 1):
            temp = one
            # one is set to a new value that is one + two
            one = one + two
            # two is set to the previous value of one
            two = temp

        return one

