sampleDic ={
    "Brand" : "Nissan",
    "Model" : "Petrol",
    "Year" : 1998,
    "Colors" : ["Black","White","Red"]
}

x = sampleDic["Model"]
print(x)
print()

y = sampleDic.get("Model")
print(y)
print()

z = sampleDic.keys()
print(z)
print()

s = sampleDic.values()
print(s)
print()

p = sampleDic.items()
print(p)
print()

if "Model" in sampleDic:
    print("Model Have this Dictionaries")