# Python Numbers

x = 1
y = 09.20
z = 9+20j

print(type(x))
print(type(y))
print(type(z))

print()
#Int
x = 1
y = 555555555555555555555555
z = -6562454524

print(type(x))
print(type(y))
print(type(z))

print()
#Float
x = 1.56
y = 6.555555555555555555555555
z = -656.2454524

print(type(x))
print(type(y))
print(type(z))

print()
x = 98e3
y = 20E9
z = -9.20e7

print(type(x))
print(type(y))
print(type(z))

print()
#Complex
x = 20+9j
y = 6j
z = -9j

print(type(x))
print(type(y))
print(type(z))

print()
#Type Conversion

x = 1
y = 09.20
z = 9+20j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print()

#Random Number

import random
print("Random Number : " ,random.randrange(1,10))