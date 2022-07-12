class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        m = prices[0]
        l = 0
        
        for i in prices[1:]:
            if i-m > l:
                l = i-m
            m = min(m, i)
                
                
        return l