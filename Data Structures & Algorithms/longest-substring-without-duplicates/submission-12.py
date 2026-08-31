class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_win = set()
        max_length = 0
        left = 0

        for right in range(len(s)):


            while s[right] in curr_win:
                curr_win.discard(s[left])
                left += 1
            
            curr_win.add(s[right])
            max_length = max(max_length, len(curr_win))
        
        return max_length
        
        