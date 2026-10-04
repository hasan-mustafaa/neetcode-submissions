class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int, {0:1})
        curr_sum = 0
        num_subarrays = 0

        for num in nums:

            curr_sum += num

            if curr_sum - k in prefix_sum:
                num_subarrays += prefix_sum[curr_sum - k]

            prefix_sum[curr_sum] += 1
        
        return num_subarrays




        
        