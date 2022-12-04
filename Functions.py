#Calling a Function
def my_fun():
    print("Hello Mark")

my_fun()

#Pass Arguments
def my_fun1(fname):
    print(fname + " Henry")

my_fun1("Mark")

#Number of Arguments
def my_fun2(fname,lname):
    print(fname + " " + lname)

my_fun2("Mark", "Henry")

#Arbitrary Arguments
def my_fun3(*cars):
    print("The favourite vehical is : " +cars[1])

my_fun3("Ford", "Benz","Toyota","Nissan")

#Keyword Arguments
def my_fun4(vehi1,vehi2,vehi3):
    print("The favourite vehical is : "+vehi3)

my_fun4(vehi1="Nissan", vehi2="BMW", vehi3="Toyota")

#Arbitrary Keyword Arguments
def my_fun5(**vehic):
    print("Favourite vehical is : "+vehic["brand"])

my_fun5(brand ="Nissan" ,model="Y62")

#Default Parameter Value
def my_fun6(brand1 = "Subaru"):
    print("We Love : " +brand1)

my_fun6("Toyota")
my_fun6()
my_fun6("BMW")

#Passing a List as an Argument
def my_fun7(vehical):
    for x in vehical:
        print(x)
vehical = ["Ford", "Nissan","BMW"]

my_fun7(vehical)

#Return Values
def my_fun8(y):
    return 13 * y

print(my_fun8(4))

#Recursion
def my_fun9(j):
    if(j>0):
        result = j +my_fun9(j-1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion" )
my_fun9(4)


#Pass
def my_fun10():
    pass #definition no content we use pass