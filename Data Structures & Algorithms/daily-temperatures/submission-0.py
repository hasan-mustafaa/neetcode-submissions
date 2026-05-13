class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        for i,temp in enumerate(temperatures):
            for n in range(i + 1,len(temperatures)):
                if temperatures[n] > temp:
                    result[i] = n - i
                    break
        return result