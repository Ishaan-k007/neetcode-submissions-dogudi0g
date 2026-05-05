"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # A deep copy is a new graph (cant just return the same nodes) with the same values as the original graph
        
        # hashmap to store node to copy relationship
        oldToNew = {}

        def dfs(node):
            # if node already in the hashmap i.e. it already has a copy return the copied one present in the hashmap
            if node in oldToNew:
                return oldToNew[node]

            # create a new copy if the copy doesnt exist
            copy = Node(node.val)
            
            # map the old node to the copy 
            oldToNew[node] = copy
            
            # for every one of the nodes neighbours call the dfs function if a copy is present it will return a copy 
            # if a copy is not present it will create a new copy and then recursively call the function on its neighbours
            # eventually each of the node neighbours will be appended to the copy nodes neighbours list 
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

