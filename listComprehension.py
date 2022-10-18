#List Comprehension

#lambda function in python
'''
def square(x):
    return x*x
res = square(5)
print(res)
'''
res = lambda x:x*2
print(res(5))

#list comprehension
l = [1,2,3,4,5]
#square the list element
'''
for i in l:
    print(i*i, end=" ")
'''
l = [1,2,3,4,5]
final_list = [x*x for x in l]
print(final_list)

#two list
l1 = [1,2,3]
l2 = [4,5,6]
final_list = [(x,y) for x in l1 for y in l2]
print(final_list)

#filter in python
#filters always return the output in list, tuple and set
#syntax: filter(lambda,list)
l = [1,2,3,4,5,6]
'''
for i in l:
    if i%2!=0:
        print(i, end=" ")
'''
final_list = tuple(filter(lambda x:x%2==0, l))
print(final_list)


#map function in python
l1 = [10,20,30,40,50]
#output [110,120,130,140,150]
'''
for i in l:
    print(i + 100, end=" ")
'''
#map always return output in form of list, tuple and set
#map(conditon,list)
final_list = list(map(lambda x:x+100,l1))
print(final_list)


#reduce function in python
import functools
l = [1,2,3,4,5,6,7,8,9,10]

'''summ = 0
for i in l:
    summ = summ + i
print("the sum of the elements are: ",summ)

n =int(input("enter the element"))
summ = 0
for i in range(1,n+1):
    summ = summ + i
print(summ)
'''
#print(dir(functools))
#SYNTAX: functools.reduce(lambda,list)
l = [1,2,3,4,5,6,7,8,9,10]
final_list = functools.reduce(lambda a,b:a+b, l)
print("The reduced output of given list is: ",final_list)

print(sum(l))
l = [1,2,3,4,105,99,5,6,7,8,9,10]
print(max(l))

final_list  = functools.reduce(lambda  a,b: a if a>b else b, l)
print("The max output of reduce list is :",final_list)

import math
print(dir(math))

import pandas
print(dir(pandas))