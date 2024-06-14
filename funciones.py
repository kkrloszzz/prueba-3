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
    pass

def exportar_archivo():
    pass

def salir():
    print("GRACIAS ADIOS!")
    exit()