class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def bt(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return

            for i, x in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                if used[i]:
                    continue
                used[i] = True
                path.append(x)
                bt(path, used)
                path.pop()
                used[i] = False



        bt([], [False]*len(nums))
        return res