vehical ={
    "Brand" : "Nissan",
    "Model" : "Petrol",
    "Year" : 1998,
    "Colors" : ["Black","White","Red"]
}

print(vehical)
for x in vehical:
    print(x)

print()
for y in vehical:
    print(vehical[y])

print()
for z in vehical.values():
    print(z)

print()
for t in vehical.keys():
    print(t)

print()
for a,b in vehical.items():
    print(a,":",b)