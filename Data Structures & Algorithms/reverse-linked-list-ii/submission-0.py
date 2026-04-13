class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        def reversing(reverse_head, left, right):
            count = right - left + 1
            prev = None
            cur = reverse_head

            while count > 0:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                count -= 1

            return prev, cur

        dummy = ListNode(0, head)
        cur = dummy
        index = 1

        # move to node BEFORE left
        while index < left:
            cur = cur.next
            index += 1

        dum1 = cur              # node before left
        start = cur.next        # first node to reverse

        reverse_head, list3_head = reversing(start, left, right)

        dum1.next = reverse_head
        start.next = list3_head

        return dummy.next
        

