class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        ret = ""
        for i, x in enumerate(strs[0]):
            for j in strs:
                if i >= len(j) or j[i] != x:
                    return ret
            ret += x
            
        return ret
        