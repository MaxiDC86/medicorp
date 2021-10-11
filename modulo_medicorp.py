import os; clear = lambda: os.system('cls'); clear()
import sys


class max_attempts_reached(Exception):
    pass


def login(lista_usuarios,lista_contrasenias,error=0):
    """
    IN: lista de usuarios y lista de contraseñas.
    OUT: acceso permitido o denegado True/False + usuario + contraseña.
    """
    permitido=False
    usuario=input("Ingrese su usuario: ")
    contrasenia=input("Ingrese su contraseña: ")
    e_usuario=lista_usuarios.count(usuario)   #Cuenta las veces que aparece el usuario en la lista
    while e_usuario==0:    #Si no aparece
        error=error+1
        print("Datos incorrectos, por favor vuelva a ingresar sus datos")
        usuario=input("Ingrese su usuario: ")
        contrasenia=input("Ingrese su contraseña: ")
        if error==3:
            print("Limite de intentos alcanzados, acceso dengado")
            permitido=False
            break
        e_usuario=lista_usuarios.count(usuario)
    else:
        pos_usuario=lista_usuarios.index(usuario)   #Si aparece busca la posicion
        while usuario not in lista_usuarios or pos_usuario==-1 or contrasenia!=lista_contrasenias[pos_usuario]:
            error=error+1
            if error==3:
                print("Limite de intentos alcanzados, acceso denegado")
                permitido=False
                break
            print("Datos incorrectos, por favor vuelva a ingresar sus datos")
            usuario=input("Ingrese su usuario: ")
            contrasenia=input("Ingrese su contraseña: ")
            pos_usuario=lista_usuarios.index(usuario)
        else:
            permitido=True

    return permitido,usuario

def menu():
    print("""
    ****** Bienvenid@ al menu de Medicorp ******
    Ingrese a una de las siguientes opciones con el número asignado:
    1 para alta de paciente,
    2 para alta de turno,
    3 para modificar datos del paciente,
    4 para baja de paciente,
    5 para listar turnos según dia y mes,
    6 para listar pacientes,
    7 para buscar turno según DNI,
    8 para cargar datos de prueba,
    0 para salir del programa.
    ******************************************************************
    """)
    while True:
        try:
            menu_selection = input()
            assert (menu_selection.isnumeric() == True) ,"Debe ingresar un número"
            menu_selection = int(menu_selection)
            assert (menu_selection>= 0 and menu_selection <=9), "Opción ingresada incorrecta"
        except AssertionError as error:
            clear()
            print(error)
        else:
            break
    return menu_selection

def modificar_paciente(modificar_datos_dni):
    try:
        pacientes = open('.\medicorp\datos_pacientes.txt','r')
    except IOError:
        print("No se pudo leer el archivo")
    else:
        linea = pacientes.readline()
        while linea != '':	
            linea = linea.rstrip()
            paciente = linea.split(';')
            dni = paciente[0]
            if dni == modificar_datos_dni:
                pacientes = open('.\medicorp\datos_pacientes.txt','w')
                apellido = input("Ingrese apellido del paciente: ")
                nombre = input("Ingrese nombre del paciente: ")
                edad = int(input('Ingrese edad del paciente: '))
                paciente= [str(dni),apellido.capitalize(), nombre.capitalize(), str(edad)]
                paciente = ';'.join(paciente)
                pacientes.write(paciente)
                print(f'Paciente con DNI {dni} modificado con exito.')
            linea = pacientes.readline()
    finally:
        print()
        exit = input("Presione enter para continuar al menu principal")
    
def listar_pacientes():
    try:
        pacientes = open('datos_pacientes.txt','r')
    except IOError:
        print("No se pudo leer el archivo")
    else:
        print("Listado de pacientes en el sistema: ")
        linea = pacientes.readline()
        while linea != '':	
            linea = linea.rstrip()
            paciente = linea.split(';')
            dni = int(paciente[0])
            apellido = paciente[1]
            nombre = paciente[2]
            edad = int(paciente[3])
            print(f'DNI:{dni:08d} APELLIDO: {apellido:<15s}' + 
            f'NOMBRE: {nombre:<15s} EDAD: {edad:02d}')
            linea = pacientes.readline()
    finally:
        print()
        exit = input("Presione enter para continuar al menu principal")

def cargar_pacientes_dni():
    try:
        pacientes = open('.\medicorp\datos_pacientes.txt','r')
    except FileNotFoundError:
        print("El archivo de paciente no se encuentra.")
    except:
        print("Error inesperado")
    else:
        lista_dni = []
        linea = pacientes.readline()
        while linea != '':	
            linea = linea.rstrip()
            paciente = linea.split(';')
            dni = int(paciente[0])
            lista_dni.append(dni)
            linea = pacientes.readline()
    return lista_dni

def alta_paciente():
    lista_dni = cargar_pacientes_dni()
    try:
        pacientes = open('.\medicorp\datos_pacientes.txt','a')
    except:
        print("Error inesperado")
    else:
        dni = int(input('Ingrese el DNI del paciente: '))
        while dni in lista_dni:
            dni = int(input('ERROR: el dni ingresado ya existe. Ingrese el DNI del paciente: '))
        apellido = input('Ingrese el apellido del paciente: ')
        nombre = input('Ingrese el nombre del paciente: ')
        edad = int(input('Ingrese edad del paciente: '))
        while edad <=17:
            print("La edad mínima es 18 años.")
            edad = int(input('Ingrese edad del paciente: '))
        paciente= [str(dni),apellido.capitalize(), nombre.capitalize(), str(edad)]
        paciente = ';'.join(paciente)
        pacientes.write(paciente + '\n')
    finally:
        print()
        exit = input("Presione enter para continuar al menu principal")

def run():
    pass

if __name__ == '__main__':
    run()