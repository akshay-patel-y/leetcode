class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r, l = 0, len(matrix) - 1
                
        while r != l and not r > l:
            row = (r + l) //2

            if matrix[row][0] <= target <= matrix[row][-1]:
                return target in set(matrix[row])
            if target < matrix[row][0]:
                if row == 0:
                    break
                l = row - 1
            else:
                r = row + 1
        if r == len(matrix):
            return False
        return target in set(matrix[r])
        
        
        