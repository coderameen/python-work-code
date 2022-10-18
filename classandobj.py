class Student:
    usn = 23
    name = 'Bob'
    branch = 'ISE'
    def displayFunc(self):
        print("This is my class function/method")

#object of class
s1 = Student()
print("The USN is: ",s1.usn)
print("The NAME is :",s1.name)
print("The BRANCH is:",s1.branch)
s1.displayFunc()


class MyClass:
    n = 40
    a = 'abc'
    def myFunc(self):
        n = 90
        print("This is functiton")
        print("Local variable: ",n)
        print("instance variable: ",self.n)

obj1 = MyClass()
print("Instance VARIABLE/class variable/attribute",obj1.n)
obj1.myFunc()

#To create Constructor in python
class Student:
    #constructor
    def __init__(self,n1,n2):
        self.num1 = n1
        self.num2 = n2
    def printFunc(self):
        print("The num1 : ",self.num1)
        print("The num2: ",self.num2)
#object
s1 = Student(80,90)
s1.printFunc()

class Sample:
    def add(self,a,b):
        self.n1 = a 
        self.n2 = b 
        print("The sum of nums: ",self.n1 + self.n2)
    

obj = Sample()
obj.add(20,30)

obj2 = Sample()
obj2.add(60,80)


class Ise:

    def studentDetails(self, usn, name, age, marks):


        #local variables
        self.usn = usn
        self.name = name
        self.age = age
        self.marks = marks 
        print("The usn: {}, name: {}, age: {} and marks:{}".format(self.usn,self.name,self.age,self.marks))
s1 = Ise()
s1.studentDetails('is01','Alen','22','99')
s2 = Ise()
s2.studentDetails('is01','Bob','22','95')