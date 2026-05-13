class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair: [temp,index]

        for curr_index,curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = curr_index - prev_index
            #Add to stack if small
            stack.append(curr_index)
     
        return result