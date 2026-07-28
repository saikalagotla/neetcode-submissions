# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def invert(self, root):
        if(root == None):
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invert(root.right)
        self.invert(root.left)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        return self.invert(root)