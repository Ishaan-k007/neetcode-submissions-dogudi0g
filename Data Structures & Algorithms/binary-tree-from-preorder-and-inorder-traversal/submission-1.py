# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        ## preorder - contains next subroots inorder
        ## inorder - order is leaf - subroot - leaf 

        # find the next root in preorder
        # at the index of that element in inorder everything on left is in left subtree everything on right is in right subtree
        #!! for preorder uptill and including mid is left and after mid is right   
        # for left subtree pass in val from start of inorder to mid (non-inclusive)
        # for right subtree pass in val from mid (non-inclusive) - to end of inorder

        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])

        mid = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
        

        
        

                
                        
                
        