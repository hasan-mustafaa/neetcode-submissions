# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length += 1
        

        prev = dummy
        curr = head

        for n in range(0, length - n):
            prev = curr
            curr = curr.next
  
        prev.next = prev.next.next

        return dummy.next
        