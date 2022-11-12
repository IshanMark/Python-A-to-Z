print("Unpacking a Tuple")
vehical = ("Ford","Nissan","Toyota")
print(vehical)

print()
(first, second, third) = vehical
print(first)
print(second)
print(third)

print("\nUsing * Mark")
(fir,sec,*thi) = vehical

print(fir)
print(sec)
print(thi)