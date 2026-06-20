# Create student class that takes name and marks of 3 objects as arguments in constructor. Then create a method to print tge average

class Student:
    def __init__(self, name, mark1,mark2,mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
    
    def average(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3
    
s1=Student("lily",34,67,43)
print(s1.name,s1.mark1,s1.mark2,s1.mark3)
print(s1.average())



# debit, credit,ptinting..method

class bank:
    def __init__(self, balance, account):
        self.balance = balance
        self.account = account

    def debit(self, amount):
        self.balance -= amount
        print("debit is:", amount)
    
    def credit(self, amount):
        self.balance += amount
        print("credit is:", amount)

man1=bank(2444,5678)
print(man1.balance,man1.account)
print(man1.debit(466))
print(man1.credit(453))
    