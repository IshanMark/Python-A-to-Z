#List 
print("List")

simList =["Apple","Mango", "Banana", "Apple"]
print(simList) #print list
print(len(simList)) #print List length
print(type(simList)) #print type

print()
simList1 =list(("Apple","Mango", "Banana", "Apple")) #dobuble () and use List Word
print(simList1)

print(simList1[1]) #Access Items
print(simList1[-2]) #-1 refers to the last item

print(simList1[1:3]) #Range
print(simList1[1:])
print(simList1[:3])

if "Apple" in simList1:
    print("Yes Have") #check itme include the list

print()
#Change List Item
print(simList1)
simList1[1]= "Orange" #[1:3]
print(simList1)

print()
#Insert Item
print(simList1)
simList1.insert(2, "Peanuts")
print(simList1)
simList1.append("BMW")
print(simList1)

print()
#extend List
print(simList)
print(simList1)
simList.extend(simList1)
print(simList)

print()
#add Any Iterable
testList = ["BMW", "Nissan", "Toyota"]
testTuple = ("Honda", "Ford")
testList.extend(testTuple)
print(testList)

print()
#Remove Specified Item
print(testList)
testList.remove("BMW")
print(testList)
testList.pop(1)
print(testList)
testList.pop()
print(testList)
del testList[0]
print(testList)
del testList
#print(testList) cant't List is Now undefined

print(simList1)
simList1.clear()
print(simList1)

print()
#Loop Lists
print(simList)
for x in simList:
    print(x)

print()
for y in range(len(simList)):
    print(simList[y])

print()
z=0
while z <len(simList):
    print(simList[z])
    z+=1

print("Looping Using List Comprehension")
[print(t) for t in simList]