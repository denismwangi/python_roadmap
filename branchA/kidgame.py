print("test yourself")
question1 = 10
question2 = 20
question3 = 30

print("2 x 10 =")
ans1 = eval(input())
if ans1 == question1:
    print("Right")
    print("question 2: 4 x 5 =")
    ans2 = eval(input())
    if ans2 == question2:
        print("Right")
        print("question 3 : 3 x 10 =")
        ans3 = eval(input())
        if ans3 == question3:
            print("right")
        elif ans1 != question1:
            print("wrong")



"""
print("there you go")
print("question 1: 2 x 5 =")
answer1 = eval(input())
if answer1 == question1:
    print("Right")

else:
    print("Wrong correct answer is ", question1)
    print("Question 2: 2 x 10")
    answer2 = eval(input())
    if answer2 == question2:
        print("Right")
    else:
        print("Wrong! the correct answer is", question2)
        print("Question 3: 3 x 10 ")
        answer3 = eval(input())
        if answer3 == question3:
            print("Right")
        else:
            print("Wrong! the correct answer is", question3)
            print("game Over!")


"""