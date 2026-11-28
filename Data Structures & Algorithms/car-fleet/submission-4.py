class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:   

        fleets = sorted(zip(position, speed), reverse=True)
        stack = []

        for pos, spd in fleets:
            time_to_reach = (target - pos) / spd
            if not stack:
                stack.append(time_to_reach)
            """
            Can replace stack with previous highest value, lead time variable, 
            reassign to current time_to_reach everytime it runs
            """
            if time_to_reach > stack[-1]:
                stack.append(time_to_reach)
            


        return len(stack)
