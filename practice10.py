f=open("pra10.txt","r")
var=f.read()
print(var)

new_var=var.replace("Java","Python")
print(new_var)

f=open("pra10.txt","w")
f.write(new_var)



word="learning"
f=open("pra10.txt","r")
data=f.read()
if(data.find(word)!=-1):
    print("Found")
else:
    print("Not Found")