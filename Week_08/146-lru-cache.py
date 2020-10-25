def __init__(self, capacity: int):
        self.capacity=collections.OrderedDict()
        self.remain= capacity

    def get(self, key: int) -> int:
        if key not in self.capacity:
            return -1
        else:
            v=self.capacity[key]
            self.capacity.pop(key)
            self.capacity[key]=v
            return v

    def put(self, key: int, value: int) -> None:
        if key in self.capacity:
            self.capacity.pop(key)
        else:
            if self.remain>0:
                self.remain-=1
            else:
                self.capacity.popitem(last=False)
        self.capacity[key]=value