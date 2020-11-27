num = eval(input("enter a number in range of 9999"))

if num < 0:
    num = 0
    if num > 9999:
        num = 9999
print(end="[")

digit = num // 100
print(digit, end="")
num %= 1000

digit = num // 100
print(digit, end="")
num %= 100

digit = num // 10
print(digit, end="")
num %= 10

print(num, end="")

print("]")

dividend = eval(input("please enter  numbers"))
divisor = eval(input("please enter 44 numbers"))
if divisor != 0:
    print(dividend, '/', divisor, "=", dividend/divisor)
else:
    print('division by zero not allowed')
