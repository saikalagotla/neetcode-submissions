# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def findMaxDepth(self, root):
        if(root == None):
            return 0
        
        left = self.findMaxDepth(root.left) + 1
        right = self.findMaxDepth(root.right) + 1

        return max(left, right)


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.findMaxDepth(root)
