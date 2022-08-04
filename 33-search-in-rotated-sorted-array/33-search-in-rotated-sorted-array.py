class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        s, e = 0, len(nums) - 1
        
        
        while s <= e:
            
            mid = e - (e-s)//2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] >= nums[s]:
                
                if target >= nums[s] and target <= nums[mid]:
                    e = mid -1
                else:
                    s = mid + 1
            elif nums[mid] <= nums[e]:
                
                if target >= nums[mid] and target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1
                    
                    
        return -1