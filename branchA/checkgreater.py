print("enter five numbers")
num1 = eval(input("enter a number one"))
num2 = eval(input("enter a number two"))
num3 = eval(input("enter a number three"))
num4 = eval(input("enter a number four"))
num5 = eval(input("enter a number five"))


if num1 > num2 or num1 > num3 or num1 > num4 or num1 > num5:
    print("greater number is", num1)
else:
    print("the minimum value is", num1)
if num2 > num1 and num2 > num3 and num2 > num4 and num2 > num5:
    print("the greater number is", num2)
else:
    print("the minimum is", num2)
    if num3 > num1 and num3 > num2 and num3 > num4 and num3 > num5:
        print("greater number is ", num3)
    else:
        print("the minimum value is", num3)

        if num4 > num1 and num4 > num2 and num4 > num3 and num4 > num5:
            print("greater number is", num4)
        else:
            print("the minimum value is", num4)
            if num5 > num1 and num5 > num2 and num5 > num3 and num5 > num4:
                print("greater value is", num5)
            else:
                print("minimum number is", num5)





