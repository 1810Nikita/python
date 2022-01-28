from random import random


import random
A="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
a="abcdefghijklmnopqrstuvwxyz"
num="1234567890"
special="!@#$%^&*()_"
all=A+a+num+special
length=16
password="".join(random.sample(all,length))
print(password)
