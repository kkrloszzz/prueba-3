import os, time 

trabajadores = []
cargos = ("CEO", "DESARROLLADOR", "ANALISTA")


while True:
    print("Menú Trabajadores")
    print("1. Registrar trabajador")
    print("2. Listar todos los trabajadores")
    print("3. Imprimir Planilla Sueludo ")
    print("4. Salir")
    opc = int(input("Ingrese opción: "))
    os.system('cls') 
    if opc == 1:
        print("REGISTRO TRABAJADOR")
        nombre_apellido = input("Ingrese Nombre Y Apellido: ")
        cargo = int(input("Ingrese Cargo (1: CEO, 2: DESARROLLADOR, 3: ANALISTA)"))
        sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100 * sueldo_bruto)
        desc_afp =  int(12/100 * sueldo_bruto)
        sueldo_liquido= sueldo_bruto-(desc_salud+desc_afp)
        trabajador  = [nombre_apellido,cargos[cargo-1],sueldo_bruto,desc_afp,desc_salud,sueldo_liquido]
        print("TRABAJADOR REGISTRADO!")



    elif opc ==2:
        pass
    
    
    
    elif opc ==3:
        pass
    
    
    else:
        os.system('cls')
        print("Nos vemos!")
        break
    time.sleep(3)
    