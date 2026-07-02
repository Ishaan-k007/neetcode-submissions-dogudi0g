class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        # pass down the max root seen:
        
        def dfs(root,max_root):
            nonlocal count 

            if not root:
                return 
            if root.val >= max_root:
                count += 1
                max_root = root.val

            dfs(root.left, max_root)
            dfs(root.right, max_root)

            
            return 
        dfs(root,root.val)
        return count


        



            


        