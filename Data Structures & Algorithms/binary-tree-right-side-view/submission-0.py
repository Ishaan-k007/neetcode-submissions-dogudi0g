# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # print root
        # level by level what is the most right most element in that level

        if not root:
            return []

        queue = deque()
        queue.append(root)
        res = []
        while len(queue) > 0:
            print(queue)
            rightmost_element = queue[-1]
            res.append(rightmost_element.val)
            for i in range(len(queue)):
                ## standard bfs stuff
                cur = queue.popleft()

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            
        return res
            ## append rightmost element at the end of level - popright of queue


        