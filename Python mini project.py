# Guess the num
import random

target=random.randint(100,200)
while True:
    userguess=int(input("Guess the number, baby:"))
    if userguess == target:
        print("Good Babe")
        break
    elif userguess > target:
        print("Take small number, babe....")
    else:
        print("Take big number, babe......")

print("Game over, sweetheart....")



# Quit the game
import random

target=random.randint(100,200)
while True:
    userguess=input("Guess the number or Quit(Q), baby:")
    if(userguess=="Q"):
        break

    userguess=int(userguess)
    if userguess == target:
        print("Good Babe")
        break
    elif userguess > target:
        print("Take small number, babe....")
    else:
        print("Take big number, babe......")

print("Game over, sweetheart....")



#Random Passoword Generator
import random
import string

pass_len=8
suggested_pass=string.ascii_lowercase+string.hexdigits+string.punctuation

passoword=""
for r in range (pass_len):
    passoword+=random.choice(suggested_pass)
print("Baby, your passoword is: " + passoword)


