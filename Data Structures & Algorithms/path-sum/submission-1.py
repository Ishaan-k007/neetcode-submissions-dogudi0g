class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        
        
        def traverse(root,cur_sum,targetSum):
            
            if root is None:
                return False

            cur_sum += root.val

            if root.left is None and root.right is None:
                return cur_sum == targetSum

            left = traverse(root.left,cur_sum,targetSum)
            right = traverse(root.right,cur_sum,targetSum)

           
            
            
            

            return left or right

        return traverse(root,0,targetSum)