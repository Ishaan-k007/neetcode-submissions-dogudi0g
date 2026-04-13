# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # one from front one from back
        # split into 2 lists the first from start -> mid then second one is reversed from mid -> end
            # find mid
            # store head of start
            # reverse linked list 
            # merge 2 lists

        # find mid
        dummy = ListNode(0,head)
        cur = head
        prev = dummy 

        fast_pointer = head
        slow_pointer = head 
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        # current slow pointer = head of second list 
        second_list_head = slow_pointer.next
        slow_pointer.next = None
        prev_second = None
        cur2 = second_list_head
        while cur2:
            temp = cur2.next
            cur2.next = prev_second
            prev_second = cur2
            cur2 = temp

        #PREV SECOND now head NOT CUR2 (NONE)
    
        first = head
        second = prev_second   # <-- reversed head

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

            
         


        

             

        