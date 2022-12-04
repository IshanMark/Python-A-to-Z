#Python does not have array we use List

car = ["BMW","Toyota","Nissan","Ford"]

#Access the element
x=car[0]
print(x)
y=len(car)
print(y)

#Looping Array element
for x in car:
    print(x)

#Adding element in the array
car.append("Ferari")
print(car)

#Remove Element
car.pop(1)
print(car)

car.remove("BMW")
print(car)