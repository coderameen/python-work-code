#Dictionary
#Emplty Dictionary
d ={}
print(d)
print(type(d))

#create a dictionary
d = {'usn':'01','name':'alen','branch':'ise'}
print(d)


#to access the dictionary
print(d['name'])


#Traversing of dict
d = {'usn':'01','name':'alen','branch':'ise'}
for key in d:
    print(key,":",d[key])

#ADDING element inside the dictionary
d = {1:10,2:20,3:30}
d[4] = 40
print(d)

print(len(d))#length

#Update element inside the dictionary
d = {'usn':'01','name':'alen','branch':'ise'}
d['name'] = 'bob'
print(d)

#old_dic.update(new_dictionary)
d1 = {1:10,2:20,3:30}
d2 = {4:40,5:50}
d1.update(d2)
print(d1)


#Deleting the element from the dictionary
'''
1. pop(key)
2. del statement
'''
#1.pop(key)
d1 = {1:10,2:20,3:30}
print(d1.pop(2))

#2. del statement
d1 = {1:10,2:20,3:30}
#del d1
print(d1)

#items()
d1 = {1:10,2:20,3:30}
print(d1.items())

#keys()
print(d1.keys())

#values()
print(d1.values())