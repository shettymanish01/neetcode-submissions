class TimeMap:

    def __init__(self):
        self.store = defaultdict()
        # res = [float("inf"), ""]
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            vals = self.store[key]
            l, r = 0, len(vals) - 1
            res = 0
            while l <= r:
                mid = l + (r - l)//2
                if vals[mid][0] <= timestamp:
                    if res != 0:
                        print(res)
                        print((timestamp - vals[mid][0]))
                        res = vals[mid] if ((timestamp - vals[mid][0]) < (timestamp - res[0])) else res
                    else:
                        res = vals[mid]
                    l = mid + 1
                else:
                    r = mid - 1
        else:
            return ""

        return res[1] if res != 0 else ""