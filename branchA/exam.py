class Example:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b


dennis = Example(8, 6)
print(dennis.add())
