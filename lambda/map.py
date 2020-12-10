a = [1,2,3,4,5]
b= [1,2,3,4,6]

c = map(lambda x: x*2, a)
print(list(c))

#same

c = [x*2 for x in a]
print(c)