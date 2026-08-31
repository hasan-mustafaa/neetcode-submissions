class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #At max there can be 3 elements that are more than n/3
        num_freq = defaultdict(int)

        for n in nums:
            num_freq[n] += 1

        threshold = len(nums) // 3

        return [num for num,freq in num_freq.items() if freq > threshold]