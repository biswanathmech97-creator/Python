collection = {1,2,2,2,3,4,"hello","hi"}

print(collection)
print(type(collection))
print(len(collection))

collection = set()
print(type(collection))

collection.add(2)
collection.add(5)
collection.add(4)
collection.add(8)
collection.add("Aff")
collection.remove(5)

print(collection)

collection.clear()
print(collection)

collection={"ferr","ghh","yuu"}
print(collection.pop())
print(collection.pop())



set1= {1,2,3,4}
set2= {3,6,7,8}
print(set1.union(set2))
print(set1)
print(set2)
print(set1.intersection(set2))