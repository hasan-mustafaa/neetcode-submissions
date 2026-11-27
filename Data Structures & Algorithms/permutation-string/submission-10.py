from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        s1_count = Counter(s1)
        s2_map = Counter()

        for right in range(len(s2)):
            s2_map[s2[right]] += 1
            
            if (right - left + 1) > len(s1):
                s2_map[s2[left]] -= 1
                left += 1
            
            if (right - left + 1) == len(s1):
                if s1_count == s2_map:
                    return True
        
        return False
