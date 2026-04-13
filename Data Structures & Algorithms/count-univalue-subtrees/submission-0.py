class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        count = 0

        def traversal(root):
            nonlocal count 
            if root == None:
                return True
            
            left = traversal(root.left)
            right = traversal(root.right)

            if left and right:
                if root.left and root.val != root.left.val:
                    return False
                if root.right and root.val != root.right.val:
                    return False
                count += 1
                return True
            return False
            
        traversal(root)
        return count