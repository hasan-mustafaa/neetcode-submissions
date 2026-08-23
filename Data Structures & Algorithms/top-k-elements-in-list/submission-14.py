
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        bucket = [[] for i in range(len(nums) + 1)]
        for num,tally in count.items():
            key = tally
            bucket[key].append(num)
        
        result = []

        for key_value in range(len(nums), 0,-1):
            for num in bucket[key_value]:
                if len(result) != k:
                    result.append(num)
        return result



        


