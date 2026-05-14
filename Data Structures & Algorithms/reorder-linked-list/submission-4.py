# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        list1 = head
        curr = head
        length = 0

        while curr:
            curr = curr.next
            length += 1

        midpoint = length // 2
        
        for node in range(0,midpoint):
            list1 = list1.next
        
        list2 = list1.next
        list1.next = None
        list1 = head

        #Reversing List
        prev = None
        curr= list2

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        list2 = prev

        #Combing List
        while list1 and list2:
            next1 = list1.next
            next2 = list2.next
            list1.next = list2
            if next1:
                list2.next = next1
            list1 = next1
            list2 = next2



        
                


