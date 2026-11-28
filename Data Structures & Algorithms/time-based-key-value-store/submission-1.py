class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        entries = self.store[key]
        l, r = 0, len(entries) - 1
        fetched_string = ""

        while l <= r:
            mid = (l + r) // 2
            curr_timestamp = entries[mid][1]
            curr_value = entries[mid][0]

            if curr_timestamp == timestamp:
                return curr_value
            elif curr_timestamp < timestamp:
                fetched_string = curr_value
                l = mid + 1
            else:
                r = mid - 1

        return fetched_string
        
