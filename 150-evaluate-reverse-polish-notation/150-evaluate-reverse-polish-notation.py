class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ops = []
        nums = []
        
        
        for i in tokens:
            x = i
            if i.isdigit() or x.lstrip('-+').isdigit():
                nums.append(int(i))
            else:
                x = 0
                y = 0
                if nums:
                    y = nums.pop(len(nums)-1)
                if nums:  
                    x= nums.pop(len(nums)-1)
         
                if i == "/":
            
                    nums.append(int(x/y))
                if i == "*":
                    nums.append(x*y)
                if i == "+":
                    nums.append(x+y)
                if i == "-":
                    nums.append(x-y)
        return nums[0]
                       
                