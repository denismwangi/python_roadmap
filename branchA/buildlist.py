def make_list():
    result = []
    in_val = 0

    for in_val in range(1, 5):
        in_val = int(input("enter integer"))
        if in_val >= 0:
            result = result + [in_val]
    return result



""""
    while in_val >= 0:
        in_val = int(input("enter integer greater than 0"))
        if in_val >= 0:
            result = result + [in_val]  # add item to the list
    return result
"""


def main():
    col = make_list()
    print(col)


main()
