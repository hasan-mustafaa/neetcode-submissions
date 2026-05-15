class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, max_profit = 0, 0

        for right in range(len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)
            else:
                left = right
        
        return max_profit

        