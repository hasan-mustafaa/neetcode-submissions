class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #K Replacements: Length of Window - Num Valid(Keep) < K(Allowed Changes)
        left = 0
        char_map = defaultdict(int)
        l_substring = 0
        max_freq = 0

        for right in range(len(s)):
            char_map[s[right]] += 1
            max_freq = max(max_freq, char_map[s[right]])


            while (right - left + 1) - max_freq > k:
                char_map[s[left]] -= 1
                left += 1
            
            l_substring = max(l_substring, right - left + 1)
        
        return l_substring


