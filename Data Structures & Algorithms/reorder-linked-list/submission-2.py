# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow_pointer = head
        fast_pointer = head
        l1 = head

        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        

        
        # slow pointer is at middle
        # reverse second half of list
        # then combine 2 lists based on indexing
        # have to split

        l2 = slow_pointer.next
        slow_pointer.next = None
        prev = None

        while l2:
            temp = l2.next
            l2.next = prev
            prev = l2
            l2 = temp

        # reversed list with prev as head
        l2 = prev 
        
        # combine 2 lists:

        while l2:
            temp1 = l1.next
            temp2 = l2.next

            l1.next = l2
            l2.next = temp1

            l1 = temp1
            l2 = temp2
                

        