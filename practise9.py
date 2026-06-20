# waf to print the length of a list

cities=["dhaka","rajshahi","noakhali","barishal"]

def print_len(cities):
    print(len(cities))

print_len(cities)


# waf to print the elements of a list in a single line. (list is the parameter)

def calc_list(cities):
    for item in cities:
        print(item, end=" ")

calc_list(cities)
print()


# waf to find the factorial of n

def calc_fact(n):
    fact=1
    for r in range(1,n+1):
        fact=fact*r
    print(fact)

calc_fact(6)


# waf to convert USD to INR

def calc_change(n):
    res=83*n
    print(res)

calc_change(5)


# waf to find out odd and even

def calc_check(n):
    if(n%2==0):
        print("Even")
    else:
        print("Odd")

calc_check(4)

# recursion

# war function to calculate the sum of first n natural num

def sum(n):
    if(n==0 or n==1):
        return 1
    else:
        return n+ sum (n-1)
    
print(sum(4))

# war function to print all elements in a list

def list(list,idx):
    if(idx==len(list)):
        return (list(idx))
    else:
        return list,(idx+1)
    
fruit=["a","b","c"]
print(fruit)

