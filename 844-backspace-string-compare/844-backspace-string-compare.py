class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(s):
            ret = ""
            
            for i in s:
                if i == "#":
                    ret = ret[:len(ret)-1]
                else: 
                    ret += i
            return ret
        return helper(s) == helper(t)
        