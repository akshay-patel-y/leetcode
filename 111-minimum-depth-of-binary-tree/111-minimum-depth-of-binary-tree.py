# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        
        curr = [root]
        n = []
        x = 1
        if not root:
            return 0
        while curr:
            for i in curr:
                if not i:
                    continue
                if not i.left and not i.right:
                    return x
                n.append(i.left)
                n.append(i.right)
            x +=1
            curr = n
            n = []
        return x
            
        