file = open("data.txt", "r")
content = file.read()
print(content)

for i in range(0, 5, 2):
    print(str(i) + " Hello")

i = 0
while i != 5:
    print(str(i) + " while loop index")
    i += 1