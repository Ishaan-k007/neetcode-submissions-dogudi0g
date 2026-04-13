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
        if head is None:
            return None
        cur = head 
        hash_map = {}
        while cur:
            node = Node(cur.val)
            hash_map[cur] = node
            cur = cur.next
        
        cur = head
        
        while cur:
            node = hash_map[cur]
            node.next = hash_map.get(cur.next)
            node.random = hash_map.get(cur.random)
            cur = cur.next

        return hash_map[head] 

        



        
        