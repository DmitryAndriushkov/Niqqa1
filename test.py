import math 

a = int(input("Enter the number A: "))
b = int(input("Enter the number B: "))
c = int(input("Enter the number C: "))

d = b * b - 4 * a * c

if d == 0:
    x1 = (-b) / (2 * a)
    x2 = x1
    print(x1, x2)

elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(x1, x2)

elif d < 0:
    print("There is no roots")
