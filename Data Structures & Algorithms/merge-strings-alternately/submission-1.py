class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_string = ""

        if len(word1) < len(word2):
            shorter_word = word1
            longer_word = word2
        else:
            shorter_word = word2
            longer_word = word1
        
        for i in range(len(shorter_word)):
            combined_string += word1[i]
            combined_string += word2[i]
        
        l = len(shorter_word)
        combined_string += longer_word[l:]

        return combined_string




        