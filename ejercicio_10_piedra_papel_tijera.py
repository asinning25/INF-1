import random

opciones = ["piedra", "papel", "tijera"]

usuario = input("Elige piedra, papel o tijera: ").lower()
computadora = random.choice(opciones)

print(f"La computadora eligió: {computadora}")

if usuario not in opciones:
    print("Opción no válida")
elif usuario == computadora:
    print("¡Empate!")
elif (usuario == "piedra" and computadora == "tijera") or \
     (usuario == "papel" and computadora == "piedra") or \
     (usuario == "tijera" and computadora == "papel"):
    print("¡Ganaste!")
else:
    print("Perdiste")
