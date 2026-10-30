usuariocorrecto = "Yohana"
clavecorrecta = "2510"

usuario = input("Introduce el nombre de usuario: ")
clave = input("Introduce la contraseña: ")

if usuario == usuariocorrecto and clave == clavecorrecta:
    print("Acceso concedido")
elif usuario == usuariocorrecto and clave != clavecorrecta:
    print("Contraseña incorrecta")
else:
    print("Usuario no encontrado")
