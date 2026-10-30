# Pedir los tres lados
a = float(input("Lado 1: "))
b = float(input("Lado 2: "))
c = float(input("Lado 3: "))

if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print("Triángulo equilátero (tres lados iguales)")
    elif a == b or a == c or b == c:
        print("Triángulo isósceles (dos lados iguales)")
    else:
        print("Triángulo escaleno (ningún lado igual)")
else:
    print("Los lados no pueden formar un triángulo")
