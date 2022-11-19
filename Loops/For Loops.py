vehical =[
    "Brand" , "Nissan",
    "Model" , "Petrol",
    "Year" , 1998
]

for x in vehical:
    print(x)

print()
for y in "1998": #Only String
    print(y)

print()
for z in vehical:
    print(z)
    if z == "Model":
        break

print()
for t in vehical:
    if t == "Model":
        break
    print(t)

print()
for s in vehical:
    if s == "Model":
        continue
    print(s)

print()
#Range
for o in range(6):
    print(o)

print()
#Range 0, 0+3, 0+3+3,....
for n in range(0,20,3):
    print(n)


#pass ,  also for loop can not empty use pass key word
for x in [0, 1, 2]:
  pass