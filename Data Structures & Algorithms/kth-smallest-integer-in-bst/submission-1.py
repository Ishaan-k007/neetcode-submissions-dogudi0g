# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # store everythoing in an array and then find the kth smallest
        # we can do an inorder traversal store it in a list and then pick out the kth element



        traversal = []

        def dfs(node):

            if node is None:
                return None

            nonlocal traversal

            left = dfs(node.left)
            traversal.append(node.val)
            right = dfs(node.right)


        dfs(root)
        return traversal[k-1]

