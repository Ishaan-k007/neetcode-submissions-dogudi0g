class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_so_far):
            if node is None:
                return 0
            
            # check if current node is good
            if node.val >= max_so_far:
                good = 1
            else:
                good = 0
            
            # update max for children
            max_so_far = max(max_so_far, node.val)
            
            left = dfs(node.left, max_so_far)
            right = dfs(node.right, max_so_far)
            
            return good + left + right
        
        return dfs(root, root.val)
        



            


        