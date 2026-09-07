class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        curr = []
        curr_sum = 0

        candidates.sort()
        def backtrack(i):
            nonlocal curr
            nonlocal curr_sum

            if curr_sum == target:
                res.append(curr[:])
                return

            
            if curr_sum > target or i >= len(candidates):
                return

            for index in range(i, len(candidates)):
                if index > i and candidates[index] == candidates[index-1]:
                    continue  # skip duplicate sibling at this level


                curr_sum += candidates[index]
                curr.append(candidates[index])
                backtrack(index + 1)
                curr_sum -= candidates[index]
                curr.pop()
            
        backtrack(0)
        return res

            