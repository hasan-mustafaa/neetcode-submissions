from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_freq = defaultdict(int)

        for num in nums:
            num_freq[num] += 1
            if num_freq[num] > len(nums) / 2:
                return num
     