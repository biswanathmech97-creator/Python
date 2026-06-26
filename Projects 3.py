# what,how,list,flowchart

import random

# (Fake Near Headline Generator)

## What Build? = fake+funny=list of words
## How? = subjects, actions, object(place)

sub = ["Baby", "China", "Cat"]
action = ["cry", "produce", "drink"]
places = ["toilet", "modi", "bear"]

while True:
    subject = random.choice(sub)
    action_choice = random.choice(action)
    place_choice = random.choice(places)

    headline = f"Breaking News: {subject} {action_choice} {place_choice}"
    print(headline)

    user_input = input("DO YOU WANT FAKE NEWS? (Yes/No) ").strip().lower()
    if user_input == "no":
        break

print("Goodbye")


# Calculator
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if(y==0):
        return("Error")
    else:
        return x/y
    

while True:
    print("CALCULATION START....")
    print("1.Add:")
    print("2.Sub:")
    print("3.multiply:")
    print("4.Divide:")
    print("5.stop")

choice=input("What do you want?1/2/3/4").strip()
if(choice==5):
    print("Goodbye")
    break
if choice in('1','2','3','4'):
    num1=float(input("1st num is:"))
    num2=float(input("2nd num is:"))

if(choice==1):
    print(f"result is:{num1}+{num2}={add(num1,num2)}")
if(choice==2):
      print(f"result is:{num1}-{num2}={sub(num1,num2)}")
if(choice==3):
    print(f"result is:{num1}*{num2}={multiply(num1,num2)}")
if(choice==4):
    print(f"result is:{num1}/{num2}={add(num1,num2)}")
else:
    print("Wrong Input....")

    