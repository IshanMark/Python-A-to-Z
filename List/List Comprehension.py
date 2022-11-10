print("List Comprehension")

simList =["Apple","Mango", "Banana", "Apple" ,"Nissan"]
newList = []

for t in simList:
    if "a" in t:
        newList.append(t)

print(newList)
print()

newList2 = [j for j in simList if "A" in j]
print(newList2)

print()
newList3 = [i for i in simList if i !="Apple"]
print(newList3)

print()
newList4 = [x for x in simList]
print(newList4)

print()
newList5 = [g.upper() for g in simList]
print(newList5) 

print()
newList6 = [u if u!="Mango" else "Banana" for u in simList]
print(newList6)

print()
newList7 = ['Mark' for k in simList]
print(newList7)

print()
newList8 = [y for y in range(5)]
print(newList8)

print()
newList9 = [z for z in range(5) if z<2]
print(newList9)