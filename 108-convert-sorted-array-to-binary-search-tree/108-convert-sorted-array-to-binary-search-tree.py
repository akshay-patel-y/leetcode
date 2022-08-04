# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def treeMaker(nums):
            if not nums:
                return None
            spot = len(nums) // 2
            tree = TreeNode(nums[spot])
            tree.right = treeMaker(nums[spot+1:])
            tree.left = treeMaker(nums[:spot]) 
            return tree
        return treeMaker(nums)