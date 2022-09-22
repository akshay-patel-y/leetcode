class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        ret = []
        
        for i in nums:
            if ret == []:
                ret.append(i)
                continue
            ret.append(max(i, i + ret[-1]))
        return max(ret)
            
        