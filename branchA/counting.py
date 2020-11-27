count = 1
while count <= 3:
    print(count)
    count += 1


entry = 0
sum = 0

print("enter numbers to sum, negative numbers")
while entry >= 0:
    entry = eval(input())
    if entry >= 0:
        sum += entry
        print("sum =", sum)

