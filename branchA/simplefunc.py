def prompt():
    print("please enter int value:", end="")


def count_to_n(n):
    for i in range(1, n + 1):
        print(i)


def better_prompt():
    num = int(input("please enter a number"))
    return num


print("this prog")
prompt()
value1 = int(input())
prompt()
value2 = int(input())
prompt()
sum = value1 + value2
print(value1, "+", value2, "=", sum)

print("counting to ten")
count_to_n(10)

print("adding two numbers")
num1 = better_prompt()
num2 = better_prompt()
total = num2 + num1
print(num1, "+", num2, "=", total)