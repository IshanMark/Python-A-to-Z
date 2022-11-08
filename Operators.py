#Arithmetic Operators
a=10
b=3

print("Arithmetic Operators")
print(a+b)  #Addition
print(a-b)  #Subtraction
print(a*b)  #Multiplication
print(a/b)  #Division
print(a%b)  #Modilus
print(a**b) #Exponentiation a^b
print(a//b) #Floor Division

print()
#Assignment Operators
print("Assignment Operators")
c= 10
c+=3 #c=c+3
print(c)
c-=5 #c=c-5
print(c)
c*=5 #c=c*3   
print(c)
c/=2 #c=c/3
print(c)
c%=3 #c=c%3
print(c)
c**=5 #c=c**3
print(c)
c//=3 #c=c//3
print(c)

d=6
d &= 4
print(d)
d |= 2
print(d)
d ^= 3
print(d)
d >>= 3
print(d)
d <<= 3
print(d)

print()
print("Comparison Operators")
#Comparison Operators
e=5
f=8
print(e==f)
print(e!=f)
print(e>f)
print(e<f)
print(e>=f)
print(e<=f)

print()
print("Logical Operators")
#Logical Operators
g=5
h=7

print(e>f and d<h)
print(e>f or d<h)
print(not(e>f and d<h))

print()
print("Identity Operators")
#Identity Operators
print(g is h)
print(g is not h)

print()
print("Membership Operators")
#Membership Operators
i=[4,6,7,8,9]
j=4
print(j in i)
print(j not in i)