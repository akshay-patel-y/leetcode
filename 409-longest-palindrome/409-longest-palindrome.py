from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        r = Counter(s)
        found = False
        s = 0
        for i in sorted(r.values())[::-1]:
            if i%2 != 0:
                if found == False:
                    s += i
                    found = True
                else:
                    s += (i-1)
            else:
                s += i
        return s
            
        