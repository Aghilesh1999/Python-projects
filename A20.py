#elif header

a = float(input("enter the value of a:"))
b = float(input("enter the value of b:"))
c = float(input("enter the value of c:"))
if a>b and a>c:
    print("a is maximum")
elif b>a and b>c:
    print("b is maximum")
else:
    print("c is maximum")
