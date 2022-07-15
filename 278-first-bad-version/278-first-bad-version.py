# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        left, right = 0, n
        ret = n
        while left <= right:
            pivot = left + (right - left) // 2
            if isBadVersion(pivot):
                ret = pivot
            if isBadVersion(pivot):
                right = pivot - 1
            else:
                left = pivot + 1
        return ret
        