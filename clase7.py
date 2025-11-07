import random
numero_secreto = random.randint(10, 50)

intento = 0
intentos = 5

adivinado = False
numero_min = 10
numero_max = 50

while intento < intentos:
    
    entrada_valida = False
    while not entrada_valida:
        try:
            numero_usuario = int(input(f"Intento {intento + 1}/{intentos}. Ingrese un numero del {numero_min} al {numero_max}: "))
            if numero_min <= numero_usuario <= numero_max:
                entrada_valida = True
            else:
                print(f"Número fuera de rango. Ingrese un número entre {numero_min} y {numero_max}.")
        except ValueError:
            print("Entrada no válida. Ingrese solo números enteros.")
            
    intento += 1 
    if numero_usuario == numero_secreto:
        print("Adivinaste")
        adivinado = True
        break
    elif numero_usuario < numero_secreto:
        print("El numero es mayor.")
    else:
        print("El numero es menor.")
if not adivinado:
    print("Perdiste. El número era:", numero_secreto)