class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l = 0
        r = len(people) - 1
        boat_count = 0

        while l <= r:
            if r == l:
                boat_count += 1
                break
                
            weight = people[l] + people[r]

            if weight > limit:
                boat_count += 1
                r -= 1
            elif weight <= limit:
                boat_count += 1
                r -= 1
                l += 1
        return boat_count





        