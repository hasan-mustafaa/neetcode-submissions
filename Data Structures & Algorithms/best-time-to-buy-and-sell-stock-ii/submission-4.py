class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        profit = 0

        for n in range(len(prices) - 1):
            right = left + 1
            if (prices[right] > prices[left]):
                profit += prices[right] - prices[left]
            left = right
        
        return profit


        