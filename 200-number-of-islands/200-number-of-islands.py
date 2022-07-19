class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        
        
        visited = [[False for i in grid[0]] for j in grid]
        r = len(grid)
        c = len(grid[0])
        
        def dfs(i, j):
            
            if i < 0 or j < 0 or i >= r or j >=c or visited[i][j]:
                return
            
            visited[i][j] = True
            if grid[i][j] == "0":
                return
            dfs(i - 1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        count = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    count += 1
                    
        return count
                
            
        