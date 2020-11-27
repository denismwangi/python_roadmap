from math import sqrt
from time import clock
"""
num = eval(input('enter a number'))

root = sqrt(num)

print("square root of", num, "=" ,root)
"""
print("enter your name:" , end="")
start_time = clock()
name = input()
elapsed = clock() - start_time
print(name, "it took you", elapsed, "to respond")