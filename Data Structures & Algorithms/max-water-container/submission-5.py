class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = min(heights[left], heights[right]) * (right-left)

        while left < right:
            if heights[left] < heights[right]:
                left += 1
                water_contained = min(heights[left], heights[right]) * (right-left)
                max_water = max(max_water, water_contained)
            else:
                right -=1
                water_contained = min(heights[left], heights[right]) * (right-left)
                max_water = max(max_water, water_contained)
        return max_water
            
