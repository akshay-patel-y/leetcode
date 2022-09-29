class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        pre = {i: [] for i in range(numCourses)}        
            
        for a, b in prerequisites:
            pre[b].append(a)
            
        def dfs(x):
            if visited[x]:
                return False
            visited[x] = True
            for i in pre[x]:
                if not dfs(i):
                    return False
            visited[x] = False
            pre[x] = []
            return True
        
        visited = [False for i in range(numCourses)]
        
        for i in pre:
            if not dfs(i):
                return False
        return True
            
        