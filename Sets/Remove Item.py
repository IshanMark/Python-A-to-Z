print("Remove Item")

vehicle ={"Ford","Nissan","Toyota","BMW","Honda"}
vehicle.remove("Ford")
print(vehicle)

vehicle.discard("Toyota")
print(vehicle)

x= vehicle.pop() # Remove Last Item
print(x)
print(vehicle)

vehicle.clear() #clear All Items
print(vehicle)

jeep ={"Ford","Nissan","Toyota"}
del jeep
#print(jeep) Can't Run this print now Jeep Undefined

