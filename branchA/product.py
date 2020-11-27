def prompt():
    print("enter order")

"""
def compute():
    b = a * c
    return b


prompt()
a = eval(input())
c = eval(input())
print(compute())
"""


class Product:
    def __init__(self,  amount , price):
        self._amount = amount

        self._price = price

    def get_price(self):
        total_price = self._price * self._amount
        return total_price


buy = Product

prompt()
_price = eval(input("enter price"))
_amount = eval(input("enter amount"))

print(buy.get_price())