class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        
        pre = {i: [] for i in range(numCourses)}
        
        incoming = {i: 0 for i in range(numCourses)}
        
        for a, b in prerequisites:
            pre[b].append(a)
            incoming[a] += 1
            
        queue = []
        
        for i in incoming:
            if incoming[i] == 0:
                queue.append(i)
        ret = []  
        while queue:
            q = queue.pop(0)
            for i in pre[q]:
                incoming[i] -= 1
                if incoming[i] == 0:
                    queue.append(i)
            ret.append(q)
        if len(ret) == numCourses:
            return ret
        return []
        