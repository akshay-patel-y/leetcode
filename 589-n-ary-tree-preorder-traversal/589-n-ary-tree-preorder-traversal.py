"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ret = []
        
        def helper(root):
            
            if root == None:
                return
            ret.append(root.val)
            for i in root.children:
                helper(i)
        helper(root)
        return ret
        