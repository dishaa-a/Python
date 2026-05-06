import random
import string

pass_len = 10
charVal = string.ascii_letters + string.digits + string.punctuation
#print(charVal)

password = " "
for i in range(pass_len):
    password += random.choice(charVal)

print("Your password is :", password)    