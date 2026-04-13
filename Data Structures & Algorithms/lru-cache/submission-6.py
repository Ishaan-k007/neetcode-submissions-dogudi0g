class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = {}
        # L - (0,0) <-> (0,0) - R
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right, self.left 

        

    def remove(self,node):
        # A <-> node <-> B to A <-> B
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self,node):
        # L - a <-> b - R to L - a <-> b <-> c - R
        # NEED TO ADD CLOSET TO R 
        prev_r_node = self.right.prev
        prev_r_node.next = node
        self.right.prev = node
        node.next = self.right
        node.prev = prev_r_node

        
         
    def get(self, key: int) -> int:
        
        if key in self.hash_map:
            self.remove(self.hash_map[key])
            self.insert(self.hash_map[key])
            return self.hash_map[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.hash_map:
            self.remove(self.hash_map[key])
        self.hash_map[key] = Node(key, value)
        self.insert(self.hash_map[key])

        if len(self.hash_map) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.hash_map[lru.key]




             



        
