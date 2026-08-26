class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow_pointer = head
        fast_pointer = head

        while fast_pointer and fast_pointer.next:
            prev_slow = slow_pointer
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        
        # Split the list into two halves
        prev_slow.next = None

        prev = None
        cur = slow_pointer

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        list2_head = prev
        list1_head = head

        while list1_head and list2_head:
            tmp1 = list1_head.next
            tmp2 = list2_head.next

            list1_head.next = list2_head
            if tmp1:
                list2_head.next = tmp1
            
            list1_head = tmp1
            list2_head = tmp2