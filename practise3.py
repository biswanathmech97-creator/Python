# WAP to check if a number entered by the user is odd or even

num= int(input("num is:"))
if(num%2==0):
    print("Even")
else:
    print("Odd")

# WAP to find the greatest of 3 numbers entered by the user

num1=int(input("num 1 is:"))
num2=int(input("num 2 is:"))
num3=int(input("num 3 is:"))

if(num1>num2 and num1>num3):
    print("num1 is great")
elif(num2>num1 and num2>num3):
    print("num2 is great")
else:
    print("num3 is great") 


# WAP to check if a number is a multiple of 7 or not

num=int(input("num is:"))

if(num%7==0):
    print("num is multiple by 7")
else:
    print("num is not multiple by 7")    