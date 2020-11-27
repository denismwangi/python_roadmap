def increment(x):
    print("beginning of execution, x =", x)
    x += 1
    print("ending of increment x =", x)


def main():
    x = 5
    print(x)
    increment(x)
    print(x)


main()
