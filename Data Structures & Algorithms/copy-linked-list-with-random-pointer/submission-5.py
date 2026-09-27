"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hashmap to store old to new
        # check if it has been made in hashmap

        old_to_new = {None:None}
        dummy = head
        while dummy:
            copy = Node(dummy.val)
            old_to_new[dummy] = copy
            dummy = dummy.next
        cur = head
        while cur:
            copy = old_to_new[cur]
            copy.next = old_to_new[cur.next]
            copy.random = old_to_new[cur.random]
            cur = cur.next
        return old_to_new[head]



        