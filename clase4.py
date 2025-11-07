# comentario en linea - que no se ejecuta el codigo
valor_moneda = 1515
nombre = input("Ingrese su nombre: ")
pesos = float(input("Ingrese cantidad de pesos: "))
#print(type(pesos))
total = pesos/valor_moneda
print("Usted", nombre, "posee U$D:",round(total,2))
print(f"Usted {nombre} posee U$D: {round(total,2)}")

PI = 3.14
radio = float(input("Ingrese el valor del radio (en metros): "))
area = PI * radio ** 2
print(f"El valor del area es: {area}")

nombre2 = input("ingrese su nombre: ")
nombre3 = input("ingrese otro nombre: ")
#print("Hola " + nombre2 + " tu nombre tiene", len(nombre2),"letras")
#print(f"Hola {nombre2} tu nombre tiene {len(nombre2)} letras")

#print(f"Tu segunda letra es: {nombre2[1]}")

print(f"Hola {nombre2.upper()}")
print(f"Hola {nombre3.lower()}")
print(f"Hola {nombre2.capitalize()} y {nombre3.capitalize()}")