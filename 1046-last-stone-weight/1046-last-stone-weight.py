class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
   
        stones = [-i for i in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            else:
                heapq.heappush(stones, x-y)
                
        if stones:
            return -heapq.heappop(stones)
        return 0
        