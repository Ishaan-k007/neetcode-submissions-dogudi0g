# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, cur: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # the lowest common ancestor occurs when a split occurs 
        # if for a node both p and q are greater or lesser we continue
        # but if for a node p is smaller and q is greater or p is equal to the node and q is greater then a split occurs which is the lowest common ancestor

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else:
                return cur 
        