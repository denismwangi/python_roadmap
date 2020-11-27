name =  input('please enter your name')

print("hello", name.upper())

s = "ABCDEFGHBCDIJKLMNOPQRSBCDTUVWXYZ "
print(s)
for i in range(len(s)):
    print(s[i])

if 'A' in s:
    print('your string contain a')

print(s.count(''))
print(s.index('D'))

if s[0].isalpha():
    print("your string starts with letter")
if not s.isalpha():
    print("your string..")