import timeit

print(timeit.timeit(stmt="[0,1,2,3,4]", number=1000000))