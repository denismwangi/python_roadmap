MAX = 20
n = 1

while n <= MAX:
    factor = 1
    print(end=str(n) + ':')

    while factor <= n:
        print("factor =", factor, 'n =', n, end='')
        if n % factor == 0:
            print( factor,end='')
            print()
         #   n += 1
        factor += 1