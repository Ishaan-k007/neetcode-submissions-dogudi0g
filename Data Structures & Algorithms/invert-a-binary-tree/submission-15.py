class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # start with the root add it to the queue pop from queue reverse its children then add children to queue

        # DFS: postorder and swap on return
        # 4 5 2 

        if not root:
            return
        temp = root.right
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(temp)
        print(root.val)
        return root 


        