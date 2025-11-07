#CONDICIONAL
temperatura = float(input("Ingrese la temperatura: "))
if temperatura > 37.8:
    print("Usted tiene fiebre.")
elif temperatura >= 37.2 and temperatura <= 37.8:
    print("Usted tiene febrícula.")
elif temperatura <= 35.4:
    print("Usted tiene hipotermia.")
else:
    print("Usted no tiene fiebre.")
print ('Fin del programa.')

#MATCH
nota = input("Ingrese nota: ")
match int(nota):
    case 8:
        print("Aprobado")
    case 10:
        print("sobresaliente")
    case 5:
        print("Casi aprobas")
    case 3:
        print("Desaprobado")
    case _:
        print("Tu nota no tiene devolucion")
        
#WHILE
contador = 1
suma = 0
cant_notas = int(input("¿Cauntas notas quiere ingresar? "))
while contador <= cant_notas:
    nota = int(input(f"Ingrese nota N°{contador}: "))
    suma = suma + nota
    contador = contador + 1
print(f"Valor de contador: {contador}")
print(f"Su promedio es: {round(suma/cant_notas,2)}")

password = "Hola"
incorrecta = True
intentos = 0
nombre = input("Ingrese su nombre: ")
while incorrecta:
    password2 = input("Ingrese su contraseña: ")
    if password == password2:
        incorrecta = False
    else:
        print("Intenta de nuevo")
        intentos += 1 # intentos = intentos + 1
print(f"Hola {nombre} ingresaste al sistema luego de {intentos} intentos fallidos.")

#FOR
acumulador = 0
for i in range(3):
    nota = int(input(f"Ingrese nota N°{i+1}: "))
    acumulador += nota
print(acumulador)

acumulador = 0
for i in range(1,4):
    nota = int(input(f"Ingrese nota N°{i}: "))
    acumulador += nota
print(acumulador)

acumulador = 0
for i in range(1,11,3):
    nota = int(input(f"Ingrese nota N°{i}: "))
    acumulador += nota
print(acumulador)