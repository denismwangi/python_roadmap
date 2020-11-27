def gcd(num1, num2):
    min = num1 if num1 < num2 else num2

    largestFactor = 1
    for i in range(1, min + 1):
        if num1 % i == 0 and num2 % i == 0:
            largestFactor = i
            return largestFactor


def get_int():
    return int(input("please enter an integer:"))


def main():
    num1 = get_int()
    num2 = get_int()
    print("gcd(", num1, ",", num2, ") =", gcd(num1, num2), sep="")


main()
