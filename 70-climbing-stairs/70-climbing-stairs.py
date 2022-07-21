class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n <= 1:
            return n
        
        
        r = [0 for i in range(n)]
        r[0] = 1
        r[1] = 2
        for i in range(n):
            
            if i < 2:
                continue
                
            r[i] = r[i-1] + r[i-2]
            
        return r[-1]
            
        