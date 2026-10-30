a = int(input("Introduce el primer número: "))
b = int(input("Introduce el segundo número: "))
c = int(input("Introduce el tercer número: "))

if a > b and a > c:
    print("El mayor es:", a)
elif b > a and b > c:
    print("El mayor es:", b)
else:
    print("El mayor es:", c)
