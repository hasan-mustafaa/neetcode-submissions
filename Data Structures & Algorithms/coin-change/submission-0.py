class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        coins.sort()
        dp = [0] * (amount + 1) #We want to ensure that that all amounts from 0 to amt is included

        for amt in range(1, amount + 1):
            min_val = float("inf")
            
            for coin in coins:
                dif = amt - coin
                if dif < 0:
                    break
                min_val = min(min_val, dp[dif] + 1)
            
            dp[amt] = min_val

        

        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[amount]
