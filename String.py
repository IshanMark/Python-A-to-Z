#String

print("Mark")
print('Mark')

print()
#Assign String to Variable
a= "Mark"
print(a)

#Multiline String
b="""I am Mark, I am Undergraduage ,
I want best coder in srilanka"""

print(b)

#String are Arrays
c = "Hello Anjana"
print(a[1])

print()
#Looping Through a String
for d in "Mark":
    print(d)

print()
#String Length
e = "Hello Imasha"
print(len(e))

print()
#Check String
f = "I crush is Imasha Hansani Rupe"
print("crush" in f)
print()
if "crush" in f:
    print("Yes,'crush' word have")

print()
print("love" not in f)
print()
if "love" not in f:
    print("Nom 'love' word not have")

print()
#Slicing String
g = " Hello, Imasha  "
print(g[7:13])
print(g[:5])
print(g[7:])

print(g[-7:-2])

print()
#Upper Case
print(g.upper())
#Lower Case
print(g.lower())

print()
#Remove WhiteSpace
print(g.strip())

print()
#Replace String
print(g.replace("i", "a"))

print()
#Split String
print(g.split(","))

print()
#String Concetenation
h = "I"
i = "Really"
j = "Like"
k = "You"
l = h+i+j+k
m = h,i,j,k
print(l)
print(m)

print()
#Format
dob = 920
text = "My Name is Mark , Sal is {}"
print(text.format(dob))

#Escape Character
    #Single Quote
print("I\'m a best programmer")

    #Backslash
print("One \\Blackslash")

    #New Line
print("I Like\nImasha")

    #Carriage Return
print("I Like\rImasha")

    #Tab
print("I Like\tImasha")

    #Backspace
print("I Like \bImasha")

    #Form Feed
print("I Like \fImasha")

    #Octal Value
print("\110\145\154\154\157")

    #Hex Value
print("\x48\x65\x6c\x6c\x6f")