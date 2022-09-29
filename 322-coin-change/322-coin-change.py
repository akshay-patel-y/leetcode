class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
      
        
        dp = [float("inf") for i in range(amount + 1)]
        
        dp[0] = 0    
        for i in range(amount + 1):
            for j in coins:
                if j > i:
                    continue
                dp[i] = min(dp[i-j] + 1, dp[i])

        if dp[-1] == float("inf"):
            return -1
        return dp[-1]
                
            