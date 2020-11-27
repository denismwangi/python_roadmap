print("Help my computer doesnot work")
print("does the computer make any sounds(fans, etc)")
choice = input("or show any light? (y/n):")

# troubleshooting control logic
if choice == 'n':
    choice = input("is it plugged in? (y/n):")
    if choice == 'n':
        print("plug it in . if the trouble persists")
        print("please run this program again")
    else:
        choice = input("is the switch in the \"on\" position? (y/n):")
        if choice == 'n':
            print("turn it on if the problem persists")
            print("please run the program again")
        else:
            choice = input("does the computer has a fuse? (y/n):")
            if choice == 'n':
                choice = input("is the outlet OK? (y/n):")
                if choice == 'n':
                    print("check the outlet's circuit")
                    print("breaker or fuse, move to a")
                    print("new outlet if necessary")
                    print("if the problem persists")

                    print("pleas run this program again")
                else:
                    print("please consult the technician")
            else:
                print("check the fuse. replace if")
                print("necessary , if the problem persists")
                print("then")
                print("please run this program again")
else:
    print("please consult a technician")
