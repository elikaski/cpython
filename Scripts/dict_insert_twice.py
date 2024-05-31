class DynamicHash:
    def __init__(self):
        self.i = 0
    def __hash__(self):
        self.i += 1
        return self.i

x = DynamicHash()
d = dict()
d[x] = 1
d[x] = 2
print(d)


for _ in range(10):
    print(x in d) # sometimes True, sometimes False

