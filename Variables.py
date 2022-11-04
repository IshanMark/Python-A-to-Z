#Variables

#Creating
a=36
b='Mark'

print(a)
print(b)
print()

c=6
c='Anjana' # t is int
print(c)   # but now t is str
print()

#Casting
d = str(7)
e = int(7)
f = float(7)

print(d)
print(e)
print(f)
print()

#Get Type of Variable
g = 5.68
h = 'Imashi'
i = 96

print(type(g))
print(type(h))
print(type(i))
print()

#Single or Double Quotes
j="Gamage"
k='Gamege' #same
l= """Gamege""" #same

print(j)
print(k)
print(l)
print()

#Case-Sensitive
m = 5
M = "Mark"
print(m)
print(M)
print()

#Variable Names
mycar = "Mark"
my_car = "Mark"
_my_car = "Mark"
myCar = "Mark"
MYCAR = "Mark"
myCar2 = "Mark"
    #can't
"""
    2mycar = 'Mark'
    my-car = 'Mark'
    my car = 'Mark' 
"""

#Camel Case
myVariableName = 'Mark'
#Pascal Case
MyVariableName = 'Mark'
#Snake Case
my_variable_name = 'Mark'

#Many Values to Multiple Variables
o, p, q = "Imashi" , "Anjana" , "Gamege"
print(o)
print(p)
print(q)
print()

#One Value to Multiple Variables
r = s = t = "Computer Science"
print(r)
print(s)
print(t)
print()

#Unpack a Collection
names = ["Imashi", "Anjana", "Gamage"]
u, v, w = names
print(u)
print(v)
print(w)
print()

#Output Variable
print(u,v,w)
print(u+v+w)
print()

x=36
y=46
z= 'Mark'
print(x+y)
#print(x+z) #can't do that
print(x,z)

#Global Variables

def myfunc():
    print("My Love is " + v)

myfunc()

print()

def myFunc1():
    v="Gamage"
    print("My Cursh is " + v)
myFunc1()

print("My Cursh is "+ v)

print()

def myFunc2():
    global v
    v = 'Gamege'
myFunc2()

print("I Like " + v)




