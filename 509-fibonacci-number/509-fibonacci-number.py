class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        s = 0
        y = 0
        x = 1
        for i in range(n + 1):
            
            if i == 0 or i == 1:
                continue
                
            s = x + y
            y = x
            x = s
            
        return s
        