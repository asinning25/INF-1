edad = int(input("Introduce tu edad: "))

if edad < 13:
    print("Niño")
elif edad >= 13 and edad <= 17:
    print("Adolescente")
elif edad >= 18 and edad <= 64:
    print("Adulto")
else:
    print("Adulto mayor")
