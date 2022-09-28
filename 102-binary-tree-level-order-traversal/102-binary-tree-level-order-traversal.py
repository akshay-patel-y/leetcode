# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ret = []
        
        curr = [root]
        
        
        while curr:
            temp = []
            c = []
            for i in curr:
                if i:
                    c.append(i.val)
                    temp.append(i.left)
                    temp.append(i.right)
            curr = temp
            if c:
                ret.append(c)
        return ret