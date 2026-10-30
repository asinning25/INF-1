monto = float(input("Introduce el monto de la compra: "))

if monto > 1000:
    descuento = monto * 0.20
elif monto >= 500:
    descuento = monto * 0.10
else:
    descuento = 0

monto_final = monto - descuento

print("El monto final a pagar es:", monto_final)
