class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        ret = []
        seen = {}
        
        for i, x in enumerate(nums):
            
            if (target - x) in seen:
                ret.append(seen[target-x])
                ret.append(i)
                return ret
                
            seen[x] = i
            
        return []
            
        