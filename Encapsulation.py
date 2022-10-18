#Public class of encap
class EncapClass:
    #instance variable
    a = 10
    def encapFunc(self):
        print("This is encap function!!!")

obj = EncapClass()
print(obj.a)

#private encap class
class EncapClass:
    #instance variable
    __a = 10
    def encapFunc(self):
        print("This is encap function!!!")
        print("The private instence variables value is: ",self.__a)

obj = EncapClass()
#print(obj.__a)
obj.encapFunc()


class A:
    __a = 1000
    def display(self):
        print(self.__a)
obj = A()
obj.display()