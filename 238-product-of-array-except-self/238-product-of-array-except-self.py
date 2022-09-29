class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        prefix=[]
        postfix=[]
        ans=[]
        a=1
        for i in range(len(nums)):
            a*=nums[i]
            prefix.append(a)
        a=1
        for i in range(len(nums)-1,-1,-1):
            a*=nums[i]
            postfix.append(a)
        postfix[:]=postfix[::-1]
        for i in range(len(nums)):
            temp=1
            if i==0:
                temp=1*postfix[i+1]
                ans.append(temp)
            elif i==len(nums)-1:
                temp=1*prefix[i-1]
                ans.append(temp)
            else:
                temp=prefix[i-1]*postfix[i+1]
                ans.append(temp)
        return ans