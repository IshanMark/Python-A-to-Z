vehical ={
    "Brand" : "Nissan",
    "Model" : "Petrol",
    "Year" : 1998
}

#Add Items
vehical["Color"] = "Black"
print(vehical)
print()

#Change Value
vehical["Year"] = 2005
print(vehical)
print()

#Update Value
vehical.update({"Year":2022})
print(vehical)
print()

#Delete Item
vehical.pop("Year")
print(vehical)
print()

vehical.popitem()
print(vehical)
print()

del vehical["Model"]
print(vehical)
print()

vehical.clear()
print(vehical)

del vehical
#print(vehical) ; Vehical dic is deleted