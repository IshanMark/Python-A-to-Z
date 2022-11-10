#Copy List
print("Copy List")
firstList=["apple","Mango", "banana","ford" ,"nissan"]
print(firstList)
copyList = firstList.copy()
print(copyList)

print()
copylist1 = list(firstList)
print(copylist1)

#Join List
print("Join List")
list1 = ["m","a","r","k"]
list2 = [1,9,9,8]
print(list1)
print(list2)
list3 = list1+list2
print(list3)

print()
for t in list2:
    list1.append(t)

print(list1)

print()

list4 = ["m","a","r","k"]
list5 = [1,9,9,8]
list4.extend(list5)
print(list4)
