class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        nums.sort()
        ret = []
        for i in range(n):
            
            if i > 0 and nums[i]==nums[i-1]:
                continue
            
            l, r = i+1, n-1
            while l < r:
                s = nums[l] + nums[i] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    temp = [nums[l], nums[i], nums[r]]
                    if temp not in ret:
                        ret.append(temp)
                    l+=1
                        
        return ret