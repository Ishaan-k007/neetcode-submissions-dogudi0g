# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # base: return True is node is null
        # conditional check establish 2 boundaries around the current node left < node.val < right.
        # if the current node was the left child then it inherits the right boundary as the parents val 
        # the left boundary is the same 
        # it initially starts of at -inf to + inf (root)

        
        
        def traversal(root,left,right):
           
            if root is None:
                return True
            
            if not (left < root.val < right):
                return False

            return (traversal(root.left,left,root.val) and traversal(root.right,root.val,right))
            

       
        return traversal(root,float("-inf"),float("+inf"))

