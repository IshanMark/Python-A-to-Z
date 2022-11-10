print("Sort List")
simList =["Apple","Mango", "Banana","Ford" ,"Nissan"]
print(simList)
simList.sort()
print(simList)

print()

simList1 = [500,260,48,32,65]
simList1.sort()
print(simList1)

print()
print(simList)
simList.sort(reverse=True)
print(simList)

print()
print(simList1)
simList1.sort(reverse=True)
print(simList1)

print()
print("Customize Sort Function")


def myFun(x):
    return abs(x-50)

myList=[500,260,52,48,32,65]
myList.sort(key = myFun)
print(myList)

print()
simList2 =["apple","Mango", "banana","ford" ,"nissan"]
simList2.sort() #Case sensitive
print(simList2)

simList2.sort(key= str.lower) #Case Insensitive
print(simList2) 


