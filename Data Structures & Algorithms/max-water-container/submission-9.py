class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_stored = 0

        while l < r:
            
            curr_stored = (r - l) * min(heights[l], heights[r])
            max_stored = max(curr_stored, max_stored)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return max_stored


