# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        carry = False
        res = ListNode()
        dummy = res 
        while l1 and l2:
            new_digit = l1.val + l2.val

            if carry:
                new_digit += 1
                carry = False
            
            if new_digit > 9:
                carry = True
                new_digit -= 10
            
            res.next = ListNode(new_digit)
            res = res.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            new_digit = l1.val
            if carry:
                new_digit = l1.val + 1
                carry = False
            if new_digit > 9:
                carry = True
                new_digit -= 10
            res.next = ListNode(new_digit)
            res = res.next
            l1 = l1.next

        while l2:
            new_digit = l2.val
            if carry:
                new_digit = l2.val + 1
                carry = False
            if new_digit > 9:
                carry = True
                new_digit -= 10
            
            res.next = ListNode(new_digit)
            res = res.next
            l2 = l2.next
        if carry:
            new_digit = 1
            res.next = ListNode(new_digit)
            res = res.next


        return dummy.next
        
        