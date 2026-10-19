class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        store = self.map
        if key not in store:
            store[key] = [] #Make a new entry with that key, and empty list
        store[key].append((value, timestamp)) #If it exists, or whether we just made a new list, add the new list (list of lists)
        

    def get(self, key: str, timestamp: int) -> str:
        #Timestamp Raw Access: self.map[key][mid][1]
        # First index for the array of lists, second one is which is the list being accessed and third is the values itself
        entries = self.map[key]
        left, right = 0, len(entries) - 1
        max_timestamp = 0
        fetched_string = ""


        while left <= right:
            mid = (left + right) // 2
            curr_timestamp = entries[mid][1]
            curr_str = entries[mid][0]

            if curr_timestamp == timestamp:
                fetched_string = curr_str
                return fetched_string
            elif curr_timestamp > timestamp:
                right = mid - 1
            else:
                max_timestamp = max(max_timestamp, curr_timestamp)
                fetched_string = curr_str
                left = mid + 1
            
        
        return fetched_string



        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)