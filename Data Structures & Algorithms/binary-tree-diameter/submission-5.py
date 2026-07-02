# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # base case : leaf node return None

        # step case : for each node left + right height


        max_diameter = 0

        def dfs(root):
            nonlocal max_diameter

            if not root:
                return 0

            left_height = dfs(root.left)
            right_height = dfs(root.right)

            cur_height = left_height + right_height
            max_diameter = max(max_diameter, cur_height)
            return 1 + max(left_height,right_height)
        dfs(root)
        return max_diameter
 


                

            
            

            