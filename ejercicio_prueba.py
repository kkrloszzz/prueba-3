import os, time 
from funciones import *

while True:
    print("Menú Trabajadores")
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir Planilla Sueludo ")
    print("4. Salir")
    opc = int(input("Ingrese opción: "))
    os.system('cls') 
    if opc == 1:
        registrar_trabajador()



    elif opc ==2:
        pass
    
    
    
    elif opc ==3:
        pass
    
    
    else:
        os.system('cls')
        print("Nos vemos!")
        break
    time.sleep(3)
    