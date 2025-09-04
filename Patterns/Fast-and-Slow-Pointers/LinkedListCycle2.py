# Leetcode 142 Medium
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                # we doing this step because we want to return the start of the cycle
                # and not where fast and slow meet
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                # cycle start
                return slow

        return