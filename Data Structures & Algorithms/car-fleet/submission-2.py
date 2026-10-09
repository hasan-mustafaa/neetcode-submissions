class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []

        for position, speed in cars:
            #Calculate time to reach for all fleets
            time_to_reach = (target - position) / speed
            #If time to reach is more than the previous fleet, then add it, if less, we don't add it (becomes part of fleet)
            if not stack or time_to_reach > stack[-1]:
                stack.append(time_to_reach)

        return len(stack)
