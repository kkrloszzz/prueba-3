trabajadores = []
cargos = ("CEO", "DESARROLLADOR", "ANALISTA")

def registrar_trabajador():
    print("REGISTRO TRABAJADOR")
        nombre_apellido = input("Ingrese Nombre Y Apellido: ")
        cargo = int(input("Ingrese Cargo (1: CEO, 2: DESARROLLADOR, 3: ANALISTA)"))
        sueldo_bruto = int(input("Ingrese sueldo bruto: "))
        desc_salud = int(7/100 * sueldo_bruto)
        desc_afp =  int(12/100 * sueldo_bruto)
        sueldo_liquido= sueldo_bruto-(desc_salud+desc_afp)
        trabajador  = [nombre_apellido,cargos[cargo-1],sueldo_bruto,desc_afp,desc_salud,sueldo_liquido]
        print("TRABAJADOR REGISTRADO!")


def listar_trabajador():
    if len(trabajadores) ==0:
        print("LISTA VACIA! REGISTRE UN TRABAJADOR EN LA OPCIÓN 1")
    else:
        print("\tLISTA DE TRABAJADORES")
        for t in trabajadores
            print(f"NOMBRE: {t[0]}\nCARGO: {t[1]}\nBRUTO: {t[2]}\nSalud: {t[3]}\nAFP: {t[4]}\nLIQUIDO: {t[5]} ")

def exportar_archivo():
    if len(trabajadores)==0:
        print("LISTA VACÍA!")

    else:
        cargo = int(input("Ingrese cargo para planilla (1: CEO, 2: DESARROLLADOR, 3: ANALISTA)"))
        if cargo==1:
            with open("todos_los_trabajadores.txt","w") as archivo: 
                for t in trabajadores:
                    archivo.writeprint(f"NOMBRE: {t[0]}\nCARGO: {t[1]}\nBRUTO: {t[2]}\nSalud: {t[3]}\nAFP: {t[4]}\nLIQUIDO: {t[5]} ")




def salir():
    print("GRACIAS ADIOS!")
    exit()