def main():
    sum = 0.0
    Entries = 3
    print("please enter", Entries, "numbers:")
    for i in range(0, Entries):
        num = eval(input("enter number" + str(i) + ":"))
        sum += num
        print("average", sum / Entries)


main()
