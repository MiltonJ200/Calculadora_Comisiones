nombre = input("Cual es tu nombre? ")
ventas = round(float((input("Cuanto has vendido este mes? "))), 2)

comisiones = ventas * 13 / 100
comisiones_redondeadas = round(comisiones, 2)

print(f"Hola {nombre} tus ventas fueron ${ventas} por lo que tu comision es de ${comisiones_redondeadas}")
