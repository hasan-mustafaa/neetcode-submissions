class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, path):


            res.append(path[:])
            
            for index in range(i, len(nums)):

                if index > i and nums[index] == nums[index-1]:
                    continue 

                path.append(nums[index])
                backtrack(index + 1, path)
                path.pop()


        backtrack(0, [])
        return res