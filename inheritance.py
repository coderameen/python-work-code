#Single level  Inheritance
class Parent:
    def pdisplay(self):
        print("Parent property!")

class Child(Parent):
    def cdisplay(self):
        print("Child property!!")

c1 = Child()
c1.cdisplay()
c1.pdisplay()

#Multi level Inheritance
class GrandParent:
    def gpdisplay(self):
        print("Grand Parent property!")
class Parent(GrandParent):
    def pdisplay(self):
        print("Parent property")

class Child(Parent):
    def cdisplay(self):
        print("Child property!!")

obj =  Child()
obj.cdisplay()
obj.pdisplay()
obj.gpdisplay()


#hierarchecal inha=eritance
class Parent:
    def pdisplay(self):
        print("parent property!!")

class Child1(Parent):
    def c1display(self):
        print("Child 1 display!!")

class Child2(Parent):
    def c2display(self):
        print("Child 2 property")

class Child3(Parent):
    def c3display(self):
        print("Child 3 property")

c1 = Child1()
c1.pdisplay()

c2 = Child2()
c2.c2display()
c2.pdisplay()

c3 = Child3()
c3.c3display()
c3.pdisplay()


#Multiple Inheritance
class Father:
    def fdisplay(self):
        print("Father property")

class Mother:
    def mdisplay(self):
        print("mother property")

class Child(Father,Mother):
    def cdisplay(self):
        print("child display")

c = Child()
c.fdisplay()
c.mdisplay()
c.cdisplay()