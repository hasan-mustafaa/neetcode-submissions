class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq = [0] * 26

        for char in s:
            freq[ord(char)-ord('a')] += 1
        
        for char in t:
            freq[ord(char) - ord('a')] -= 1

        for count in freq:
            if count != 0:
                return False
        return True


        


#Create 2 dictionary, with key value pairs letter and frequency
#Then compare