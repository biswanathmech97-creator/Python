# WAP to ask the user to enter names of their 3 fanvs movie & store them in a list

movie=[]
movie1=str(input("movie1 is:"))
movie2=str(input("movie2 is:"))
movie3=str(input("movie3 is:"))

movie.append(movie1)
movie.append(movie2)
movie.append(movie3)

print(movie)



# WAP to check if a list contains a palindrome of elements.

marks=[2,5,6,7,8]
copy_marks = marks.copy()
copy_marks.reverse()

if(copy_marks==marks):
    print("Palindrome")
else:
    print("Not Palindrome") 



# WAP to sort it and count the number of students with the "A" grade in the following tuple

arr=["C","D","A","A","B","B","A"]
arr.sort()
print(arr)
print(arr.count("A"))


  