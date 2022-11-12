#Tuple
print("Tuple is a collection which is ordered and unchangeable. Allows duplicate members")

simTuple = ("Ford","Nissan","Toyota")
print(simTuple)

print()
#Allow Duplicates
print("Allow Duplicate")
simTuple1 =("Ford","Nissan","Toyota","Ford")
print(simTuple1)
print("Tuple Length")
print(len(simTuple1))

#Type
print("Type")
simTuple2 =("Ford",)
simTuple3 = ("Ford")
print(type(simTuple2))
print(type(simTuple3))

print()
print("Tuple Constructor")

simTuple4 = tuple(("Ford","Nissan","Toyota"))
print(type(simTuple4))
print(simTuple4)