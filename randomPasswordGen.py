import string
import random
from random import randint

length = randint(8,32)

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "&#{}()[]|-_ç@=+*/-.;!?$£,"
all = lower + upper + numbers + symbols
output = "".join(random.sample(all,length))

def save(output):
    print("Would you like to save your password to a text file?")
    answer = input('y/n: ')
    if answer == 'y':
        print("One moment...")
        file = open("Password.txt","a")
        file.write("\n"+output)
        file.close()
    elif answer == 'n':
        print("...")
    else:
        print("Please input y or n...")
    

print (output)
save(output)