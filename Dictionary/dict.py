my_dict = {"name":"dennis","age":27, "city":"kenya"}
print(my_dict)

value = my_dict["age"]
print(value)

my_dict["email"] = "denis@gmail.com"
print(my_dict)

#del my_dict["name"]
print(my_dict)

my_dict.popitem()
print(my_dict)

if "name" in my_dict:
    print(my_dict["name"])

try:
    print(my_dict["lastname"])
except:
    print("not found")

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key,":", value)