# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # base case : root (no more leaves) return
        # step case : keep going down both left and right but left first 
        # add to list then when return remove from list 
        # append to res if node < max of list 
        # 2,1,1 - 

        visited_nodes = []
        res = 0
        
        def traversal(root):
            nonlocal visited_nodes
            nonlocal res
            print("visited", visited_nodes)
            print("res",res)
            if root is None:
                return
            
            visited_nodes.append(root.val)
            root.left = traversal(root.left)
            print("root", root.val)
            if root.val >= max(visited_nodes):
                res += 1
            root.right = traversal(root.right)
            visited_nodes.remove(root.val)
            


        traversal(root)
        return res




            


        