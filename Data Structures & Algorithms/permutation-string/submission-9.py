from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = Counter(s1)
        curr_win = Counter(s2[:len(s1)])
        flag = True if s1_freq == curr_win else False


        for right in range(len(s1), len(s2)):

            curr_win[s2[right]] += 1
            curr_win[s2[right - len(s1)]] -= 1

            if s1_freq == curr_win:
                flag = True
                return flag
        
        return flag
        