class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        #At max there can be 3 elements that are more than n/3
        num_freq = defaultdict(int)
        threshold = len(nums) // 3
        res = []

        for n in nums:
            num_freq[n] += 1
            if num_freq[n] == threshold + 1:
                res.append(n)

        return res