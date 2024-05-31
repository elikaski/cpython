class HashCollision:
    def __init__(self, s):
        self.s = s
    def __hash__(self):
        return 1337
    def __eq__(self, other):
        print("comparing")
        self.s.add(self.s.pop() * 1)
        return False

s=set()
x=HashCollision(s)
s.add(1337)
s.add(x)
