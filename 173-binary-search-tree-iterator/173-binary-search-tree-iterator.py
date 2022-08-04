# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    k = []
    curr = 0
    def __init__(self, root: Optional[TreeNode]):
        
        def helper(root):
            if not root:
                return []
            return helper(root.left) + [root.val] + helper(root.right)
        self.k = helper(root)
        self.curr = 0
        return None
        
        
    def next(self) -> int:
        self.curr += 1
        return self.k[self.curr - 1]
        
        

    def hasNext(self) -> bool:
        if self.curr < len(self.k):
            return True
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()