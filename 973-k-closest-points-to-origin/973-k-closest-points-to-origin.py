class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def heapsort(iterable, k):
            h = []
            for value, pair in iterable:
                heappush(h, [value, pair])
            return [heappop(h)[1] for i in range(k)]
        
        p = [[(x**2 + y**2)**.5, [x,y]] for x,y in points]
        return heapsort(p, k)
        