my_dict = {"name":"dennis","age":27, "city":"kenya" ,"email":"hhhhh@"}
my_dict2 = dict(name="mary",age=44, city="boston")
my_dict3 = {2:5,5:3,9:88}

my_dict.update(my_dict2)
print(my_dict)

#use actual key when accessing value
value = my_dict3[2]
print(value)

#use also tuple as key
mytuple = (5,6)
my_dict5 = {mytuple:5}
print(my_dict5)