info={
    "key" : "value",
    "name" : "apna college",
    "learning" : "coding",
    "age" : "35",
    "is_adult": True,
    "marks" : 94.4,
    "subjects" : ["Python", "C", "Java"]
}

print(type(info))
print(info)
print(info["name"])
#print(info["surname"]) #error
info["name"]= "Bishakha"
print(info)

null_dict={}
null_dict["name"]="apna college"
print(null_dict)


# Nested Dictionaries
stu={
  "name" : "Murgi",
  "sub" : {
      "phy" : 56,
      "chem" : 76,
      "math" : 98
  }
 }

print(stu["sub"]["chem"])
print(stu.keys())
print(len(stu))
print(list(stu.keys()))
print(list(stu.values()))
print(stu.items())
print(list(stu.items()))

pairs = list(stu.items())
print(pairs[0])

print (stu.get("name"))

new_dict = {"name":"baby","age":23}
stu.update(new_dict)
print(stu)



