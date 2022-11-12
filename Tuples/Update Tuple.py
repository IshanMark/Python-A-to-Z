#Update Tuples
print("Update Tuples")

print("\nChange Value")
simTuple = ("Ford","Nissan","Toyota","Honda","Feraari","Benz")
simTuple2 = list(simTuple)
simTuple2[2] = "KIA"
simTuple = tuple(simTuple2)
print(simTuple)

print("\nAdd Items")
simTuple3 = list(simTuple)
simTuple3.append("Isuzu")
simTuple = tuple(simTuple3)
print(simTuple3)

print("\nAdd tuple to a tuple")
simTuple4 =("TVS","Yamaha")
simTuple += simTuple4
print(simTuple)

print("\nRemove Items")
simTuple5 = list(simTuple)
simTuple5.remove("TVS")
simTuple = tuple(simTuple5)
print(simTuple)

del simTuple5

#print(simTuple5) Del can't run this print