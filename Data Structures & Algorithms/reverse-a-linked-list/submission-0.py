# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterate through the list
        # Take the last node and connect it to head
        # Iterate through head + reversing
        # Easiest to use recursion no?
        # Call reverseList on Base case and reutrn back the after calls
        # return head
        # Base Case: head.next = null
        # Recursive Case: head.next != null
        # Q: how would you keep track of prev node
        trav = head
        trail = None
        while trav != None:
            temp = trav.next
            trav.next = trail
            trail = trav
            trav = temp
        return trail
