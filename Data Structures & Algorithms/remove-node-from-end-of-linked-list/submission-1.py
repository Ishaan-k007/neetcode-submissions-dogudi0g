# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = ListNode(None,head)
        cur = head 
        prev = dummy
        length = 0
        while cur:
            cur = cur.next
            length += 1

        index = length  
        target = index - n
        print("T1",target)
        index = 0
        cur = head
        while cur:
            print(index)
            if index == target:
                prev.next = cur.next
                break
            prev = cur
            cur = cur.next
            index += 1

        return dummy.next


        