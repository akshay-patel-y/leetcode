class Solution:
    def rob(self, nums: List[int]) -> int:
        
        ret = []
        
        if len(nums) <= 2:
            return max(nums)
        
        ret.append(nums[0])
        ret.append(max(nums[0],nums[1]))
        
        for i in nums[2:]:
            ret.append(max(i + ret[-2],ret[-1]))
        
        print(ret)
        return max(ret)
        