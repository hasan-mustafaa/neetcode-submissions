class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        right = len(heights) - 1
        left = 0

        while left < right:
            
            area = min(heights[left],heights[right]) * (right - left)
            if area > maxArea:
                maxArea = area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maxArea

'''
Container with most water
Container = h x w
Here h is the minimum of the left and right pointer min(l,r)
and w is the number of elements between then (right - left)
'''