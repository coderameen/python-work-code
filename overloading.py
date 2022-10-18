#Polymorphism - Overloading
'''
1. Operator overloading
2. method overloading
'''
#Operator overloading
#'+' sting(concationation), integer(adding)
# String
n1 = '10'
n2 = '20'
print(n1 + n2)#1020

a = 'hello'
b = 'Alen'
print(a+b)#helloAlen

#integer
n1 = 10
n2 = 40
print(n1 + n2)

#'*' datatypes(Replication), integers(Multiplication)
#datatypes
l = [10,20]
print(l*3)#[10,20,10,20,10,20]

#integers
n1 = 20
n2 = 30
print(n1 * n2)

#Method overloading
def add():
    n1 = 10
    n2 = 30
    summ = n1 + n2
    print("The sum is ",summ)
add()#40
def add(a,b):
    print(a - b)
add(30,20)#10
def add(x,y,z):
    print(x+y+z)

add(10,20,30)#60