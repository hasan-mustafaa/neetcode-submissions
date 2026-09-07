class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = set()

        def backtrack(i, path):

            if len(path) == len(nums):
                res.append(path[:])
                return
            

            
            for index in range(len(nums)):
                if nums[index] in visited:
                    continue
                visited.add(nums[index])
                path.append(nums[index])
                backtrack(index, path)
                path.pop()
                visited.discard(nums[index])

        
        backtrack(0,[])
        return res