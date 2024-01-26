import random
import string
import array
max_len=12
password=""
for i in range(65,91):
    password+=chr(i)
for i in range(48,58):
    password+=chr(i)
for i in range(97,123):
    password+=chr(i)
for i in range(33,40):
    password+=chr(i)



length=int(input("Enter length of a password:"))
a="".join(random.sample(password,length))
print(f"Yor password is {a}")
