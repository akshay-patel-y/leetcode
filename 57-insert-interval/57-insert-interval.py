class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        
        curr = [newInterval]
        while curr:
            x = curr.pop()
            ret = []
            print(x)
            for t in intervals:
                
                if curr:
                    ret.append(t)
                    continue
                
                if x[1] < t[0] or t[1] < x[0]:
                    ret.append(t)
                    continue
                if x[0] < t[0] and x[1] > t[1]:
                    curr.append(x)
                    continue
                if x[0] >= t[0] and x[1] <= t[1]:
                    return intervals
                if x[0] >= t[0] and x[1] > t[1]:
                    newX = t[0]
                    newY = x[1]
                    curr.append([newX, newY])
                    continue
                if x[1] <= t[1] and x[1] >= t[0] and x[0] < t[0]:
                    newX = t[1]
                    newY = x[0]
                    curr.append(sorted([newX, newY]))
                    continue
                    
            intervals = ret          
            if curr == [] and x:
                intervals.append(x)
                
        return sorted(intervals)
                
                    
        