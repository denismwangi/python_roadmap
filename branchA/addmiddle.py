entry = 0
sum = 0
print("enter number to sum")

while True:
    entry = eval(input())
    if entry < 0:
       break

    sum += entry

    print("sum", sum)