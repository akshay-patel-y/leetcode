class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        curr = ""
        m = 0
        
        for i in s:
            if i in curr:
                m = max(m, len(curr))
                curr = curr[curr.index(i)+1:]
            curr += i
        m = max(len(curr), m)      
        return m
        
        