class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        x = len(p)
        
        w = Counter(p)

        ret = []
        
        for i in range(len(s) - x + 1):
            
         
            
            t = Counter(s[i:i+x])
            
            if w == t:
                ret.append(i)
                
                
        return ret
        