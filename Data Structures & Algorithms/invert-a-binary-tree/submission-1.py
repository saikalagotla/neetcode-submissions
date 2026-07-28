# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def invert(self, root):
        if(root == None or (root.left == None and root.right == None)):
            return root
        temp = None
        if(root.left != None):
            temp = root.left
        
        root.left = root.right
        root.right = temp

        root.right = self.invert(root.right)
        root.left = self.invert(root.left)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.invert(root)