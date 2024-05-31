class DynamicHash:
    def __init__(self):
        self.i = 0
    def __hash__(self):
        self.i += 1
        return self.i

x = DynamicHash()
s = set()
s.add(x)
s.add(x)
print(s)
