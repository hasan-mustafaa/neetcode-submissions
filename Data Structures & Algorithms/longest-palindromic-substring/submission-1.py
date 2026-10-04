class Solution:
    def longestPalindrome(self, s: str) -> str:
        res_start = 0
        max_len = 0

        def expand(left, right):
            nonlocal res_start, max_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    res_start = left
                left -= 1
                right += 1

        for i in range(len(s)):
            expand(i, i)        
            expand(i, i + 1)    

        return s[res_start:res_start + max_len]