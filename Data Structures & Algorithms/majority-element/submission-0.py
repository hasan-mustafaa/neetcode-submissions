class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_freq = defaultdict(int)

        for n in nums:
            num_freq[n] += 1
        
        return max(num_freq, key=num_freq.get)
        