from random import choice

symbol = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len_password = int(input("how long would you like your password to be? enter in numbers"))
password = ""

for i in range(len_password):
    password += choice(symbol)

print(password)
#you are very bad at programming i dont like this.
