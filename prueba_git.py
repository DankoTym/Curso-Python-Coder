numero_1 = float (input("Ingrese un número: "))
numero_2 = float (input("Ingrese otro número: "))
opcion=0
while opcion != 4:
  opcion = int (input("ingrese una opcion: \n 1-Mostrar la suma de los dos números. \n 2-Mostrar la resta de los números. \n 3-Mostrar la multiplicacion de los números. \n 4-Si elige esta opción se interrumpirá la impresión del menú y el programa finalizará. \n"))
  if opcion == 1:
    print(f"La suma de sus números es {numero_1 + numero_2}")
  if opcion==2:
    print(f"La resta de sus números es {numero_1 - numero_2}")
  if opcion==3:
    print(f"La multiplicación de sus números es {numero_1 * numero_2}")
  if opcion==4:
    print("Saliendo del Menú")
    break
  if opcion<1 or opcion>4:
    print("Opción incorrecta, deberá reingresar")
print("termino la ejecucion")