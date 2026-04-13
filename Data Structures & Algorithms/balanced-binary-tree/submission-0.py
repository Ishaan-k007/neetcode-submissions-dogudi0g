# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        bool_var = True 
        def traversal(root):
            nonlocal bool_var 
            if root is None:
                return 0

            left_height = traversal(root.left)
            right_height = traversal(root.right)
            
            if abs(right_height - left_height) > 1:
                bool_var = False
            
            return 1 + max(left_height, right_height)

        traversal(root)
        if bool_var:
            return True
        return False