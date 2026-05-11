class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_window = 0
        window = 0
        left = 0
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1
                window -= 1
            
            seen.add(s[right])
            window += 1
            max_window = max(max_window, window)

        
        return max_window
        
    