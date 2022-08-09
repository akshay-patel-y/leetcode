class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        rows = len(img)
        cols = len(img[0])
        
        def avg(i, j):
            
            r = [-1, 0, 1]
            
            t = 0
            c = 0
            for x in r:
                for y in r:
                    if (i+x) < 0 or (j + y) < 0 or (i+x) >= rows or (j+y) >= cols:
                        continue
                    t += img[i+x][j + y]
                    c += 1
            return t//c
        
        ret = [[j for j in i] for i in img]
        
        for i in range(len(img)):
            for j in range(len(img[0])):
                ret[i][j] = avg(i, j)
                
        return ret
        