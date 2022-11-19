a = 96
b = 69
c = 55

if b<a:
    print("a is greater than b")
elif b>a:
    print("b is greater than a")
else:
    print("a and b is equal")

#Short Hand If
print()
if a>b: print("a is greater than b")    

#Short Hand If...Else
print()
print("A") if a>b else print("B")

#AND
print()
if a>b and c>a:
    print("Both Are true")

#OR
print()
if a>b or c>a:
    print("At Least One Con is true")

#Nested If
print()
t=41
if t>10:
    print("Above 10")
    if t>20:
        print("also above 20")
    else:
        print("but not above 20")

#Use Pass if statement can not empty
if b>a:
    pass