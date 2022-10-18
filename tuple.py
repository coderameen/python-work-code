t = (10,20,30,44,55,[10,20])
print(t)
print(type(t))

#access of element using indexing
print(t[5][1])


#Empty tuple
t = ()
print(t)
print(type(t))

t1 =(10,)
print(type(t1))

#tuple()
l = [10,20,30]
t = tuple(l)
print(t)

#Input from user in form of tuple
# t  = tuple(input("Enter the element"))
# print(t)

# t = eval(input("Enter the element"))
# print(t)

t = (10,2033,44)
#length
print(len(t))


#sorted(tuple)
t = (3,4,7,1,2)
n_t = sorted(t)
print(n_t)

#adding can't be done in tuple, bcoz tuples are immutable
t = (3,4,7,1,2)
#t[2]=30
print(t)


#Traversing of tuple
t = ('apple','mango','grapes')
for element in t:
    print(element)

#in and not in
t = ('apple','mango','grapes')
if 'appppple' in t:
    print("True")
else:
    print("False")

#Comparingt of tuple(>,<,<=,>=,==,!=)
t1= (10,20,30)
t2 = (40,50,60)
t3 =(10,20,30)
print(t1 == t2)
print(t1 ==  t3)

#min(tuple) and max(tuple)
t2 = (40,50,60)
print(min(t2))
print(max(t2))

#count(ele)
t = (11,2,55,7,888,888,888)
print(t.count(888))

#Delete element using del statement
t = (11,2,55,7,888,888,888)
#del t
print(t)


#concatination and Replication/repeatation
t1= (10,20,30)
t2 = (40,50,60)
print(t1+t2)
print(t1*3)