# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # first node instead of pointing to none needs to point to after right 

        cur = head
        before = None
        count = 1
        while count < left:
            before = cur
            cur = cur.next
            count += 1
            

        # start of reversing

        start = cur
        print(start.val)

        prev = None

        diff = 0
        while diff <= right - left :
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            diff += 1
        
        # cur is
        end = cur

        start.next = end
        
        if left == 1:
            return prev
        before.next = prev
        return head 



        