item=int(input("How Many Item in list :"))
print("list item contain:",item)

item2=int(input("How Many Item in list :"))
print("list item contain:",item2)

newlist=[]
for i in range(item):
    i = int(input())
    newlist.append(i)

for i in range(item2):
    i = int(input())
    newlist.append(i)
print("your list is:",newlist)
print(newlist[0:-2])

evenlist=[]
oddlist=[]

for i in  newlist:
    if i%2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)

print("even list is:",evenlist)
print("odd list is:",oddlist)

min_value= newlist[0]
for i in newlist:
    if i < min_value:
        min_value = i
print(min_value)

max_value=evenlist[0]
for i in evenlist:
    if i > max_value:
        max_value = i 
print(max_value)


min_value=oddlist[0]
for i in oddlist:
    if i < min_value:
        min_value=1
print(min_value)
