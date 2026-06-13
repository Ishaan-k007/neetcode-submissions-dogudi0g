class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # start with the root add it to the queue pop from queue reverse its children then add children to queue

        # DFS: postorder and swap on return 

        if not root:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root