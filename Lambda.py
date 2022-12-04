#lambda Sysntax 
# lambda arguments : expression

x= lambda a:a+55
print(x(8))

print()
y = lambda a,b : a*b
print(y(8,6))

#Lambda Function
print("\nLambda Function")
def my_fun(n):
    return lambda a: a*n

multi = my_fun(2)
print(multi(6))