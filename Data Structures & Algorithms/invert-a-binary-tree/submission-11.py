# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # start with the root add it to the queue pop from queue reverse its children then add children to queue

        if not root:
            return None
        
        queue = deque([root])

        while queue:
            node = queue.popleft()
            node.left,node.right = node.right,node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root