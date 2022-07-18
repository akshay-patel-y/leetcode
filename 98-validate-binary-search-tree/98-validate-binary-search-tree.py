# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root, min, max):
            
            if not root:
                return True
            if root.val < max and root.val > min and helper(root.right, root.val, max) and helper(root.left, min, root.val):
                return True
                
            return False
        
        return helper(root, -float("inf"), float("inf"))
        
        
                    
                    
        