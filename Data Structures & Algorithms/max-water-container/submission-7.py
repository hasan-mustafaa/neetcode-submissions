class Solution:
    def maxArea(self, heights: List[int]) -> int:
       l = 0
       r = len(heights) - 1
       max_stored = 0

       while l < r:
            if heights[l] <= heights[r]:
                stored_water = heights[l] * (r-l)
                max_stored = max(max_stored, stored_water)
                l += 1
            else:
                stored_water = heights[r] * (r-l)
                max_stored = max(max_stored, stored_water)
                r -= 1
        
       return max_stored

