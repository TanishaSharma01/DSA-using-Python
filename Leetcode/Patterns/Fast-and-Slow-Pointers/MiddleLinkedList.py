# Leetcode 876 Easy

# odd number of nodes return the middle one
# even number of nodes, return the second of the two middle nodes
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Solution 1: using a regular loop
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        current = head

        while current:
            count += 1
            current = current.next

        current = head
        for i in range(0, count // 2):
            current = current.next

        return current

# Solution 2: Using fast and slow pointers
    def middleNode2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
