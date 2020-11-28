import sys

my_list = [0,1,2, "hello" ]
my_tuple = (0,1,2,"hello")
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

