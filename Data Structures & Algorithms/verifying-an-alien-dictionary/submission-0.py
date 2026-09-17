class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderIndex = {word:index for index, word in enumerate(order)}

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]

            for j in range(len(word1)):

                if j == len(word2):
                    return False
                
                index1, index2 = orderIndex[word1[j]], orderIndex[word2[j]]
                
                if word1[j] != word2[j]:
                    if index2 < index1:
                        return False
                    break
        
        return True
                