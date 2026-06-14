from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque()
        traversal = []
        if root:
            queue.append(root)
        
        while len(queue) > 0:
            cur_traversal = []
            for i in range(len(queue)):
                
                curr = queue.popleft()
                cur_traversal.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            traversal.append(cur_traversal)
                                
        return traversal