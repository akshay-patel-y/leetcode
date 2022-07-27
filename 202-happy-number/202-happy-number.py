class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()
        while n != 1:
            x = str(n)
            temp = 0
            for i in x:
                temp += int(i)**2
            if temp in seen:
                return False
            seen.add(temp)
            n = temp
        return True
        