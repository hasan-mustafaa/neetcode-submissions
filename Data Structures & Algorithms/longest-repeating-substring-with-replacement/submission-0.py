from collections import Counter

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        curr_win = Counter()
        longest_string = 0
        limit = k

        for right in range(len(s)):

            curr_win[s[right]] += 1

            while (right - left + 1) - max(curr_win.values()) > k  :
                curr_win[s[left]] -= 1
                left += 1
            
            longest_string = max(longest_string, right - left + 1)
            

        return longest_string



        