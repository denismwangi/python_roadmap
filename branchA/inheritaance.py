class Parent:
    def __init__(self, a):
        self.a = a

    def method1(self):
        print(self.a * 2)

    def method2(self):
        print(self.a + '!!!')


class child(Parent):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def method1(self):
        print(self.a * 7)

    def method3(self):
        print(self.a + self.b)


obj1 = Parent('hi')
obj2 = child('hi', 'bye')

print('parent method1 :', obj1.method1())
print('parent methond2:', obj1.method2())
print()
print('child methond 1:', obj2.method1())
print('child methond 2:', obj2.method2())
print('child methond 3:', obj2.method3())
