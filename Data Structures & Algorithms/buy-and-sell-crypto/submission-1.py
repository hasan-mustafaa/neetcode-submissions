class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = maxProfit = curr = 0

        for right in range(len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else: 
                left = right
            
            right += 1

        return maxProfit
            
'''
Left should be min, and right should be ma
'''