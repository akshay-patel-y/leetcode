class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ret = []
        x = 0
        y = 0
        
        moves = [[0,1], [1, 0], [0,-1], [-1,0]]
        curr = 0
        currMove = moves[curr]
        def change():
            nonlocal curr
            nonlocal currMove
            curr = (curr + 1) % 4
            currMove = moves[curr]
            
        for move in range(len(matrix) * len(matrix[0])):
            if (matrix[x][y] == "Seen"):
                x = x - currMove[0]
                y = y - currMove[1]
                change()
                x = x + currMove[0]
                y = y + currMove[1]
                ret.append(matrix[x][y])
                matrix[x][y] = "Seen"
            else:
                ret.append(matrix[x][y])
                matrix[x][y] = "Seen"

            if (x + currMove[0]) >= len(matrix) or ((x + currMove[0]) < 0):
                change()
            if (y + currMove[1]) >= len(matrix[0]) or (y + currMove[1]) < 0:
                change()
            x = x + currMove[0]
            y = y + currMove[1]
            
        return ret
    

            
            
            
            
        