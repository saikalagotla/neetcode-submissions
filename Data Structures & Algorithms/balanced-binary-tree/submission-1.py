# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def getHeight(root):
            if(root == None):
                return 0
            
            left = getHeight(root.left)
            right = getHeight(root.right)

            if(abs(left-right) > 1):
                return -1
            
            if(left == -1 or right == -1):
                return -1
            
            return 1+max(left, right)

        
        res = getHeight(root)
        if(res == -1):
            return False

        return True
        

            
