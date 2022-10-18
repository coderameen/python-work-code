l = [10,20,30,[40,50,60]]
print(l)
#type of data type
print(type(l))

#length of the list
print(len(l))

#accessing the element of list]
l = [10,20,30,[40,50,60]]
print(l[3][1])

#Sclicing in list
#list_variable[start_index:end_index:step]
print(l[2:])

#l = index(ele)
l = [11,22,33,22,22,44]
print(l.index(33))

#count(ele)
l = [11,22,33,22,22,44]
print(l.count(22))

#list() 
strr = "hello"
l = list(strr)
print(l)

t = ('a',10,20)
print(type(t))
l = list(t)
print(l)

#index(ele)
l = [10,20,30]
#print(l.index(100000))

#insertion of element inside the list
'''
1.append(ele)
2.extend(ele)
3.insert(pos,ele)
'''

#l.append(ele)
l = [10,20,30]
l.append(100)
print(l)
l.append(50)
print(l)

#l.extend(ele)
l = [11,22,33]
l.extend([44])
print(l)

#l.insert(pos,ele)
l = [10,20,30,40]
l.insert(1,15)
print(l)

#Delete the element of list
'''
1. pop(<index>)
2. remove(ele)
3. clear()
4. del statement
'''

#1.pop(<index>)
l = [11,22,25,33,44]
print(l.pop(2))

#2. remove(ele)
l = [10,20,30,44,40]
l.remove(44)
print(l)

#3. clear()
l = [10,20,30,44,40]
l.clear()
print(l)

#4. del statement
l = [10,20,30,44,40]
del l

#print(l)

#count
#reverse()
l = [10,20,30,44,40]
#print(l[::-1])
#print(l.reverse())
l.reverse()
print(l)

#sort()
l= [3,2,6,9,7,1]
l.sort()
print(l)

#sorted(list)
l= [3,2,6,9,7,1]
new_list = sorted(l)
print(new_list)

#sum(list)
l = [1,2,3,4,5,6,7,8,9,10]
summ = sum(l)
print("The sum of the list are: ",summ)

#min(list) and max(list)
l = [45,87,99,105,20,15]
max_ele = max(l)
print("The max element in list is ",max_ele)

min_ele = min(l)
print("The min element in list is ",min_ele)

