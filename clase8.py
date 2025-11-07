while True:
    numero = input("Ingresa un número: ")
    
    if not numero.isdigit():
        print("Programa finalizado.")
        break
    
    numero = int(numero)
    
    if numero == 0:
        print("Programa finalizado.")
        break

    palabra = input("Ingrese una palabra: ")
    cantidad = len(palabra)
    print("Cantidad de caracteres:", cantidad)

    factorial = 1
    for i in range(1, cantidad + 1):
        factorial *= i
    print("El factorial de", cantidad, "es:", factorial)

    if factorial % 2 == 0:
        print("El factorial es PAR.")
    else:
        print("El factorial es IMPAR.")

    print("_______________________")