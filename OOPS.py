class Student:
    name="Karan" #class atribute
    roll= 45

s1= Student()
print(s1.name)
s2= Student()
print(s2.roll)


class Student:
    name="Karan"
    roll= 45
    def __init__(self):
       print("adding new stu in database..")

s1= Student()
print(s1)


class Student:

    #default cons
    def __init__(self):
        pass
    def __init__(self, fullname,marks): #parameterized constructor(self,parameter)
        self.name = fullname #define kora...instance object(diff obj)
        self.marks= marks

    def welcome(self):
        print("hi")

s1 = Student("Karan",78)
print(s1.name,s1.marks)
s2= Student("Arjun",65)
print(s2.name,s2.marks)
s2.welcome()


#del
class Student:
    name="Karan" #class atribute
    roll= 45

s1= Student()
print(s1.name)
s2= Student()
print(s2.roll)

#del s1
#print(s1)


class Bank:
    def __init__(self, balance, account_pass):
        self.balance = balance #public
        self.__account_pass = account_pass #private

    def reset_pass(self):
        print(self.__account_pass)

s1=Bank(2345, "000123")
print(s1.balance)
#print(s1.account_pass)
print(s1.reset_pass()) 



# poly
print(1+5)
print([1,6,7]+[4,7,8])
print("apna"+"college")


# complex
class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
    def shownum(self):
        print(self.real,"i","+",self.img,"j")
    def __add__(self,num2):
        newreal=self.real+num2.real
        newimg= self.img+num2.img
        return Complex(newreal,newimg)
    
num1=Complex(1,5)
num1.shownum()
num2=Complex(5,6)
num2.shownum()
num3=num1+num2
num3.shownum()



# inheritance
class Employ:
    def __init__(self, id, roll):
        self.id = id
        self.roll = roll
    def showdetails(self):
        print(self.id,"is","self.roll")
class Programmer(Employ):
    def showlanguage(self):
        print("hi")

m1= Employ("2345",(4578))
m1.showdetails()
m2= Programmer("3456","856")
m2.showdetails()
m2.showlanguage()




