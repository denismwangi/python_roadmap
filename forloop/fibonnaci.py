"""
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 . . .
not expected output
"""
num = 0
next = 0

num = eval(input('enter number'))
for i in range(num):
    next += (num + next)
    print(next)