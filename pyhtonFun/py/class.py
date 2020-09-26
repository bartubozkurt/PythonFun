class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName =firstName
        self.lastName = lastName
        self.age = age

person1 = Person("Bartu","Bozkurt",21)
print(person1.firstName,person1.lastName,person1.age)

class Worker(Person):
    def __init__(self,salary):
        self.salary = salary
class Customer(Person):
    def __init__(self,creditCardNumber):
        self.creditCardNumber = creditCardNumber
"""
bartu =  Worker()
bartu.firstName , bartu.lastName , bartu.age

"""

#-------------------------------------------#

"""
mehmet = Customer()
mehmet.firstName, mehmet.lastName , mehmet.age , ++ mehmet.creditCardNumber

"""
