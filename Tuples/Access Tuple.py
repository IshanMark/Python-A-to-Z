#Access Tuple Items

print("Access Tuple Items")
simTuple = ("Ford","Nissan","Toyota","Honda","Feraari","Benz")
print(simTuple[1])

print("\nNegative Indexing")
print(simTuple[-4])

print("\nRange of Indexes")
print(simTuple[1:3])
print(simTuple[:3])
print(simTuple[3:])

print("\nRange of Nagative")
print(simTuple[-4:-1])

print("\nCheck id Item")
if "Ford" in simTuple:
    print("Yes Have in this Tuple")

