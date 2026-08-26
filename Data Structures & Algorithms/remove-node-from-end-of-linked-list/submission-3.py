class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        cur = head
        count = 0
        while cur:
            cur = cur.next
            count += 1
        
        if count - n == 0:
            return head.next
        cur = head
        for i in range(count - n - 1):
            cur = cur.next
        
        if cur.next:
            cur.next = cur.next.next
        else:
            cur.next = None
        return head