# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        cur1 = list1
        cur2 = list2
        dummy = ListNode()
        temp = dummy
        
        



        while cur1 and cur2:
            if cur1.val > cur2.val:
                temp.next = cur2
                cur2 = cur2.next
            else:
                temp.next = cur1
                cur1 = cur1.next
            temp = temp.next

        if cur1:
            temp.next = cur1
        else:
            temp.next = cur2
        
        return dummy.next

            
        
            