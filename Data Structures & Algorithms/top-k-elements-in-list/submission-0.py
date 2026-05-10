class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        
        #Calculates frequency of each number in the array
        for num in nums:
            if num in result:
                result[num] += 1
            else:
                result[num] = 1
        
        sorted_keys = sorted(result, key=lambda x: result[x], reverse=True)

        top_k = sorted_keys[:k]

        return top_k

        
        




'''
Key Value Pair: Value: Frequency
Use dynamic array, to increment frequency
''' 

'''
Misunderstanding:
Do not return elements that occur k times
Return elements the top k most frequent elements
If k = 2, return 2 numbers, with the highest frequency
'''