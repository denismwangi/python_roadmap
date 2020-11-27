def help_screen():
    print("add: adds two numbers")
    print("subtract: subtracts two numbers")
    print("print: displays result")
    print("help: displays help screen")
    print("Quit: exits the program")


def menu():
    return input("====A)dd s)ubtract p)rint h)elp Q)uit ===")


# global variables
result = 0.0
arg1 = 0.0
arg2 = 0.0


def get_input():
    global arg2, arg1
    arg1 = float(input("enter number 1:"))
    arg2 = float(input("enter number 2:"))


def report():
    print(result)


def add():
    global result
    result = arg1 + arg2


def subtract():
    global result
    result = arg1 - arg2


def main():
    done = False;
    while not done:
        choice = menu()

        if choice == "A" or choice == "a":
            get_input()
            add()
            report()
        elif choice == "S" or choice == "s":
            get_input()
            subtract()
            report()
        elif choice == "P" or choice == "p":
            report()
        elif choice == "H" or choice == "h":
            help_screen()
        elif choice == "Q" or choice == "q":
            done = True
main()