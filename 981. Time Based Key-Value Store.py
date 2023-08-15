class TimeMap:
    def __init__(self):
        self.store = {}  # list [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        times = self.store.get(key, [])

        l, r = 0, len(times) - 1
        res = ""
        while l <= r:
            mid = (l + r) // 2
            val, t = times[mid]
            if t <= timestamp:
                res = val
                l = mid + 1
            else:
                r = mid - 1

        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
