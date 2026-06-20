# Print numbers from 1 to 100

i=1
while i<=100 :
   print(i)
   i=i+1

# print numbers 100 to 1

i=100
while i>=1 :
   print(i)  
   i=i-1

# print mulitiplication table

i=1
while i<=10 :
  print("2", "*", i, "=", 2*i)
  i=i+1

#print the elements of the following list using a loop

nums= [1,3,9,16,25,36,49,64,81,100]
i=0
while i<=9 :
   print(nums[i])
   i=i+1

# Search for a number x in this tuple using loop

nums=[1,3,6,8,3]

x=8
i=0

while i<=4 :
   if (nums[i]==x):
      print("F",i)
      break
   else:
      print("NF")
   i=i+1
      
