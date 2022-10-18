#set
s = set()
print(s)
print(type(s))


#unique set
s = {2,2,4,3,2,1}
print(s)

#set()
l = [1,2,3,60,60,7,60]
s = set(l)
print(s)

#traverse the set
s = {'alen','bob','celvin'}
for i in s:
    print(i)

#to print from 1-10
for i in range(1,11):
    print(i, end=' ')
print()
#to access the element
s = {'alen','bob','celvin'}
#print(s[1])
#NOTE: We can't access the element of set using indexing but we can access by traversing it using looping statement

#length
print(len(s))

#Add the element inside the set
#add(ele)
s = {10,20,30}
s.add(55)
print(s)

#Update element inside the set
#old_Set.update(new_set)
s1 = {10,20,30}
s2 = {40,50}
s1.update(s2)
print(s1)

#Delete tehe element of set
'''
1.remove(ele)
2.discard(ele)
3.pop()
'''
#remove(ele)
s1 = {10,20,30}
s1.remove(20)
print(s1)
#pop()
s1 = {10,20,30}
s1.pop()
print(s1)
# print(id(s1))

s1 = {10,20,30}
s1.discard(10)
print(s1)

#union or |
#s1.union(S2)
s1 = {10,20,30,40,50}
s2 = {40,50,60,70}

print(s1.union(s2))
print(s1|s2)

#intersection or &
s1 = {10,20,30,40,50}
s2 = {40,50,60,70}
print(s1.intersection(s2))
print(s1&s2)

#difference or  -
s1 = {10,20,30,40,50}
s2 = {40,50,60,70}
print(s1.difference(s2))
print(s1 - s2)
