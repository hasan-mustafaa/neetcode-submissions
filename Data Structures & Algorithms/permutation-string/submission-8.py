class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = {}
        win_freq = {}
        left = 0

        for char in s1:
            s1_freq[char] = s1_freq.get(char,0) + 1
        
        for right in range(len(s2)):
            char = s2[right]
            win_freq[char] = win_freq.get(char,0) + 1

            if right - left + 1 > len(s1):
                win_freq[s2[left]] = win_freq.get(s2[left],0) - 1

                if win_freq[s2[left]] == 0:
                    del win_freq[s2[left]]

                left += 1


            if win_freq == s1_freq:
                return True

        return False
            