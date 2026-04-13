# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        arr = []

        def traverse(root,low,high):
            nonlocal arr

            if root is None:
                return 

            if root.val >= low:
                if root.val <= high:
                    arr.append(root.val)

            left = traverse(root.left,low,high)
            right = traverse(root.right,low,high)

            return 

        traverse(root,low,high)
        return sum(arr)
        