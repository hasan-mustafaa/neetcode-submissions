class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = maxProfit = curr = 0

        for right in range(len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else: 
                '''
                Since right iterates through every datapoint, 
                if in any scenario left < right, 
                then right's current minimum
                '''
                left = right
            
            right += 1

        return maxProfit
            
'''
Left should be min, and right should be ma
'''