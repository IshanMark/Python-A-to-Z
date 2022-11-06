#Basic Booleans
print(5>4)
print(5==4)
print(5<4)

#Bool With If Else Condition
a = 55
b = 20 

print()
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

print()

#Evaluate Values and Variables
print(bool("CS"))
print(bool(920))
print(bool(["Imashi","Anjana","Gamage"]))

print()

c = "CS"
d = 920
e = ["Imashi","Anjana","Gamage"]
print(bool(c))
print(bool(d))
print(bool(e))

print()
#Some Values are False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

print()
#Functions Can Return a Booleans

def myFun():
    return True
print(myFun())
print()

if myFun():
    print("True")
else:
    print("FALSE")


x= 100
print(isinstance(x, str))