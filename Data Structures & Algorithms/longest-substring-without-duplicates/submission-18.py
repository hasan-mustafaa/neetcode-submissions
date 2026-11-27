class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_map = set()
        l_substring = 0

        for right in range(len(s)):

            while s[right] in char_map:
                char_map.discard(s[left])
                left += 1

            char_map.add(s[right])
            l_substring = max(right - left + 1, l_substring)
            
        return l_substring
            
