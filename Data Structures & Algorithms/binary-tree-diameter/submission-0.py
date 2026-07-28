# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.maxDia = 0

        def maxDiameter(root):
            if(root == None):
                return 0

            right = maxDiameter(root.right)
            left = maxDiameter(root.left)

            if(right+left > self.maxDia):
                self.maxDia = right+left

            return 1+max(left, right)
        
        maxDiameter(root)
        return self.maxDia