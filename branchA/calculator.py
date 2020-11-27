def help_screen():
    print("add: adds two numbers")
    print("subtract: subtracts two numbers")
    print("print: displays result")
    print("help: displays help screen")
    print("Quit: exits the program")


def menu():
    return input("====A)dd s)ubtract p)rint h)elp Q)uit ===")


def main():
    result = 0.0
    done = False;
    while not done:
        choice = menu()

        if choice == "A" or choice == "a":
            arg1 = float(input("enter arg1 :"))
            arg2 = float(input("enter arg2 :"))
            result = arg1 + arg2
            print(result)
        elif choice == "S" or choice == "s":
            arg1 = float(input("enter arg1 :"))
            arg2 = float(input("enter arg2 :"))
            result = arg1 - arg2
            print(result)
        elif choice == "P" or choice == "p":
            print(result)
        elif choice == "H" or choice == "h":
            help_screen()
        elif choice == "Q" or choice == "q":
            done = True


main()
