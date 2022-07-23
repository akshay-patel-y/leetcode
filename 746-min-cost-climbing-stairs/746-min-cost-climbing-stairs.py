class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        ret = [0 for i in cost]
        
        for i, x in enumerate(cost):
            if i == 0 or i == 1:
                ret[i] = cost[i]
                continue
            ret[i] = min(cost[i] + ret[i-1], cost[i] + ret[i-2])
    
        return min(ret[-1], ret[-2])
        