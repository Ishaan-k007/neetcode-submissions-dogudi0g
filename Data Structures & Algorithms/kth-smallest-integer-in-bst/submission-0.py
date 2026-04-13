# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count_arr = []

        def traversal(root,k):
                if not root:
                        return

                left = traversal(root.left,k)
                nonlocal count_arr 
                count_arr.append(root.val)
                print(count_arr)
                right = traversal(root.right,k)

                


        traversal(root,k)
        return count_arr[k-1] 
