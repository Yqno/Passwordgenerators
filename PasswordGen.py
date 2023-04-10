import random

lower = "abcdefghijklmnopkrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "#[]{}()*;/,_-"

all = lower + upper + numbers + symbols

length = 25
password = "".join(random.sample(all,length))
print(password)
