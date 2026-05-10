class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []

        for num in nums:
            if num in freq:
                freq[num] += 1;
            else:
                freq[num] = 1;
        
        sorted_freq = sorted(freq, key=lambda x: freq[x], reverse=True)
        return list(sorted_freq[:k])
