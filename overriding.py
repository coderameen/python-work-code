class Parent:
    a = 10
    def display(self):
        print("Parent property")
class Child(Parent):
    a  = 30
    def display(self):
        print("Child property")

c = Child()
print(c.a)
c.display()

