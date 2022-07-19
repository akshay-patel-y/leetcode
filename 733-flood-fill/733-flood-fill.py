class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        r = len(image)
        c = len(image[0])
        visited = [[False for i in image[0]] for j in image]
        start = image[sr][sc]
        def helper(x , y):
            nonlocal image
            if x < 0 or y < 0 or x >= r or y >= c:
                return
            
            if image[x][y] != start or visited[x][y]:
                return
            image[x][y] = color
            visited[x][y] = True
            helper(x+1,y)
            helper(x-1,y)
            helper(x,y+1)
            helper(x,y-1)
            
        helper(sr, sc)
        
        return image

        