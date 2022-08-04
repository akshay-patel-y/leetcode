class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        #setup a double ended queue
        q = deque()
        #counters for time, and remaining fresh
        time, fresh = 0,0
        #standard why to find size of grid
        rows,cols = len(grid), len(grid[0])
        #nested for loops to go thru each square in grid
        for r in range(rows):
            for c in range(cols):
                #1 means fresh orange
                if grid[r][c] == 1:
                    #so if grid is 1, increase fresh count by 1
                    fresh+=1
                #2 means rotting orange
                if grid[r][c] == 2:
                    #add co-ords of current block to q
                    q.append([r,c])
        #we need to check in 4 directions to see if rot will spread
        directions = [[0,1], [0, -1], [1,0], [-1,0]]

        #while q isn't empty and there are still fresh oranges left
        while q and fresh > 0:
            #loop thru the q
            for i in range(len(q)):
                #get last val in q for row and column
                r,c = q.popleft()
                #check dif in all directions
                for difRow, difCol in directions:
                    row = difRow + r
                    col = difCol + c
                    #if fresh orange is found in bounds, we need to make it rotten
                    if(row < 0 or row == rows or col < 0 or col == cols or grid[row][col] != 1):
                        continue
                    #if it doesn't get disqualed by any of those, make it rotten
                    grid[row][col] =2
                    #add it to q so it's included in next iter of while loop
                    q.append([row,col])
                    #if we just made an orange rotten, we need to decrease no of fresh
                    fresh-=1
            time+=1
        #return -1 if we weren't able to make all oranges rotten
        return time if fresh == 0 else -1