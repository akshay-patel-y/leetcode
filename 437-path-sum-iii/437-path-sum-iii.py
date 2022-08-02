# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        
        def dfs(root, t):
            c = 0
            if not root:
                return count
            
            if root.val == t:
                c += 1
                
            if root.left:
                c += dfs(root.left, t - root.val)
            if root.right:
                c += dfs(root.right, t - root.val)
            
            return c
        
        tc, queue = 0, [root]
        if not root:
            return 0
        while queue:
            temp = []
            for i in queue:
                tc += dfs(i, targetSum)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            queue = temp
        return tc