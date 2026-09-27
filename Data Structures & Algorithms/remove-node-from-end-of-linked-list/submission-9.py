# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # n th node from the end of the list = length of the list - n from the start
        # find length
        # find n 

        dummy = head
        length = 0
        while dummy:
            dummy = dummy.next
            length += 1
        if length == n:
            return head.next

        
        sol_index = length - n - 1

        count = 0
        temp = head 
        while temp and count < sol_index:
            temp = temp.next
            count += 1
        if temp.next.next:
            temp.next = temp.next.next
        else:
            temp.next = None
        return head 
        