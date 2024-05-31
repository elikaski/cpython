class HashCollision:
    def __init__(self, d):
        self.d = d
    def __hash__(self):
        return 1337
    def __eq__(self, other):
        print("comparing")
        del self.d[1337]
        self.d[1337] = 1
        return False

d = {1337: 1}
x=HashCollision(d)
x in d # alternatively: d[x] = 1
