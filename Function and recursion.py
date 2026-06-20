# function defination
def calc_sum(a,b):  # parameters
    sum=a+b
    print(sum)
    return sum

calc_sum(3,6) #function call; arguments
calc_sum(5,98)


#
def print_hello():
    print("hello")

#print_hello()
output=print_hello()
print(output) # None


#
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

calc_avg(4,7,8)


#
print("mommy","daddy") #sep=" "
print("mommy",end="$") #sep=" "
print("baby") #end="\n"


#
def calc_sum(a=2,b=6):  # without own value error show
    print(a*b)
    return a*b

calc_sum()


# recursion

#
def calc_res(n):
     if (n==0):  # base case
         return 
     print(n)
     calc_res(n-1)
     print("End")

calc_res(5)


#
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n-1)
    
print(fact(4))





    



