nota = float(input("Introduce la puntuación (0-100): "))

if nota < 0 or nota > 100:
    print("Error: la nota debe estar entre 0 y 100")
elif nota >= 90:
    print("A")
elif nota >= 80:
    print("B")
elif nota >= 70:
    print("C")
elif nota >= 60:
    print("D")
else:
    print("F")
