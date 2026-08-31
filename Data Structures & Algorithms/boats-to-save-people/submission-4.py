class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        
        people.sort()
        l = 0
        r = len(people) - 1
        boat_count = 0

        while l <= r:
                
            weight = people[l] + people[r]

            if weight > limit:
                boat_count += 1
                r -= 1
            elif weight <= limit:
                boat_count += 1
                r -= 1
                l += 1

        # one person left over, unpaired (Slippery, Edgecase)
        if l == r:  
            boat_count += 1

        return boat_count





        