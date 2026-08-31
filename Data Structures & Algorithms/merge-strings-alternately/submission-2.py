class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        combined_string = ""
        min_len = min(len(word1), len(word2))
        
        for i in range(min_len):
            combined_string += word1[i]
            combined_string += word2[i]
        
        combined_string += word1[min_len:] + word2[min_len:]

        return combined_string




        