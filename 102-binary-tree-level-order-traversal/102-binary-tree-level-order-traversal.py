# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ret = []
        
        nodes = [root]
        while nodes:
            temp = []
            newNodes = []
            for i in nodes:
                if i == None:
                    continue
                temp.append(i.val)
                if i.left:
                    newNodes.append(i.left)
                if i.right:
                    newNodes.append(i.right)
            nodes = newNodes
            if temp:
                ret.append(temp)
        
        return ret
        