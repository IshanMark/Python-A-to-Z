print("Join Sets")

vehi = {"Ford","Nissan","Toyota"}
num = {5, 6, 7}

print(vehi)
print(num)
vehical = vehi.union(num)
print(vehical)

vehi.update(num)
print(vehi)

samSet={"BMW","Honda","Ferrari","Daraz"}
service ={"eBay", "Ali", "Daraz"}
print("\nFind Duplicate Item")
service.intersection_update(samSet)
print(service)

samSet1={"BMW","Honda","Ferrari","Daraz"}
service1 ={"eBay", "Ali", "Daraz"}

newSet = samSet1.intersection(service1)
print(newSet)

print("\nKepp All")
newSet1 =samSet1.symmetric_difference(service1)
print(newSet1)

samSet1.symmetric_difference_update(service1)
print(samSet1)