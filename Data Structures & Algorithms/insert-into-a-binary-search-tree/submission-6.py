# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # left is smaller than the right
        # first we need to try and find the position of the value that we are adding
        
        if root is None:
            return TreeNode(val)
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()

            if val > node.val:
                if node.right:
                    queue.append(node.right)
                else:
                    node.right = TreeNode(val)
                    
            
            else:
                if node.left:
                    queue.append(node.left)
                else:
                    node.left = TreeNode(val)
        return root 
                
        