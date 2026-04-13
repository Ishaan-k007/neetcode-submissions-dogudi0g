# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        
        def traverse(root,prev_root,cur_sum):
            if root == None:
                return cur_sum

            if root.val == prev_root+1:
                cur_sum += 1
            else:
                cur_sum = 1
            
            left = traverse(root.left,root.val,cur_sum)
            right = traverse(root.right,root.val,cur_sum)

            return max(cur_sum,left,right)
        return traverse(root,0,0)


            
         

        
        
        