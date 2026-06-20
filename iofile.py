f=open("iodemo.txt", "r") 
data = f.read()
print(data)
print(type(data))
f.close()



f=open("iodemo.txt", "r") 
data = f.read(6)
print(data)
print(type(data))
f.close()


f=open("iodemo.txt", "r") 
line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
line3 = f.readline()
print(line3)
line4 = f.readline()
print(line4)
f.close()


f=open("iodemo.txt","w")
data=f.write("I want to become an Engineer")
print(data)
f.close()


f=open("iodemo.txt","a")
data=f.write("\nI want to become an cooky Engineer")
print(data)
f.close()


with open("iodemo.txt", "r") as f:
    data=f.read()
    print(data)


import os

os.remove("sample.txt")