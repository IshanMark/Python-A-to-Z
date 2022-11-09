#Built-in Data Types

"""
Text Type : str
Numeric Types : int , float, complex
Sequence Types :  list, tuple, range
Mapping Type : dict
Set Types : set, frozenset
Boolean Type: bool
Binary Types : bytes, bytearray, memoryview
None Type : NoneType

Getting Data type 
print(type(variableName))
"""

print()

# Setting the Data Type
x= "Hello Anjana"
print(x)
print(type(x))

print()
x= 1103
print(x)
print(type(x))

print()
x= 11.03
print(x)
print(type(x))

print()
x= 5+ 7j
print(x)
print(type(x))

print()
x= ["Imasha","Hansani","Rupe"]
print(x)
print(type(x))

print()
x= ("Imasha","Hansani","Rupe")
print(x)
print(type(x))

print()
x= range(6)
print(x)
print(type(x))

print()
x= {"Name": "Anjana", "DOB": 20000911}
print(x)
print(type(x))

print()
x= {"Name", "Anjana", "DOB", "20000911"}
print(x)
print(type(x))

print()
x= False
print(x)
print(type(x))

print()
x= bytearray(9)
print(x)
print(type(x))

print()
x= memoryview(bytes(9))
print(x)
print(type(x))

print()
x= None
print(x)
print(type(x))

#Setting the Specific Data Type

print()
y = str("Hello Anjana")
print(y)
print(type(y))

print()
y = int(2000)
print(y)
print(type(y))

print()
y = float(2000.0920)
print(y)
print(type(y))

print()
y = complex(9+20j)
print(y)
print(type(y))

print()
y = list(("Imasha","Hansani","Rupe"))
print(y)
print(type(y))

print()
y = tuple(("Imasha","Hansani","Rupe"))
print(y)
print(type(y))

print()
y = range(20)
print(y)
print(type(y))

print()
y = dict(Name = "Anjana", DOB= 20000920)
print(y)
print(type(y))

print()
y = set(("Imasha","Hansani","Rupe"))
print(y)
print(type(y))

print()
y = frozenset(("Imasha","Hansani","Rupe"))
print(y)
print(type(y))

print()
y = bool(20)
print(y)
print(type(y))

print()
y = bytes(20)
print(y)
print(type(y))

print()
y = bytearray(20)
print(y)
print(type(y))

print()
y = memoryview(bytes(20))
print(y)
print(type(y))

