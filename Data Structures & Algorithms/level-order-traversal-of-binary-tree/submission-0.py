# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        
        queue = deque()

        queue.append(root)
        res = []
        
        while len(queue) > 0:
            print(queue)
            cur_list = []

            for i in range(len(queue)):
                cur_list.append(queue[i].val)
            res.append(cur_list)
            
            for i in range(len(queue)):
               
                
                cur_element = queue.popleft()
                
                if cur_element.left:
                    queue.append(cur_element.left)
                    
                if cur_element.right:
                    queue.append(cur_element.right)
            
                    
                
            
      
      
        
        return res



# 1 in queue pop in res and children to queue
# for each child 
        