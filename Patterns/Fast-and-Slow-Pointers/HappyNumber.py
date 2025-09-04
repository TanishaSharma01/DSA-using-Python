# Leetcode 202 Easy

class Solution:
    def getNext(self, n: int) -> int:
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit * digit
            n //= 10
        return sum

    # Solution 1: With Fast and Slow Pointers
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.getNext(n)

        while fast != 1 and slow != fast:
            slow = self.getNext(slow)
            fast = self.getNext(self.getNext(fast))

        return fast == 1

    # Solution 2: With Hashset
    def isHappy2(self, n: int) -> bool:
        numbers = set()
        numbers.add(n)
        pointer = self.getNext(n)

        while pointer != 1:
            if pointer in numbers:
                return False
            numbers.add(pointer)
            pointer = self.getNext(pointer)

        return True


