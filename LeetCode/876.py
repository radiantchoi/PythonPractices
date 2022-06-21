# LeetCode No.876 Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from math import ceil

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        trav = head
        while trav.next:
            trav = trav.next
            n += 1
        
        target = math.ceil(n / 2)
        
        result = head
        while target > 0:
            result = result.next
            target -= 1
        
        return result