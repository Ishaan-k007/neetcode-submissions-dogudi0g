class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # start with the root add it to the queue pop from queue reverse its children then add children to queue

        # DFS: postorder and swap on return
        # 4 5 2 

        if not root:
            return
        
        q = deque([root])
        cur = root

        while q:
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            temp = node.right
            node.right = node.left
            node.left = temp
        return cur


        