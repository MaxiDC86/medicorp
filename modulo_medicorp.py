import os; clear = lambda: os.system('cls'); clear()
import sys


class max_attempts_reached(Exception):
    pass


def login(lista_usuarios,lista_contrasenias):
    """
    IN: lista de usuarios y lista de contraseñas.
    OUT: acceso permitido o denegado True/False + usuario + contraseña.
    """
    error = 2
    usuario=input("Ingrese su usuario: ")
    while usuario not in lista_usuarios:    #Si no aparece en la lista vuelve a pedir el usuario.
        error=error-1
        print("Datos incorrectos, por favor vuelva a ingresar sus datos")
        usuario=input("Ingrese su usuario: ")
        if error==0:
            print("Limite de intentos alcanzados, acceso dengado")
            return False,usuario
    contrasenia=input("Ingrese su contraseña: ")
    pos_usuario=lista_usuarios.index(usuario)   #Si aparece busca la posicion
    while contrasenia!=lista_contrasenias[pos_usuario]:
        error=error-1
        if error==0:
            print("Limite de intentos alcanzados, acceso denegado")
            return False, usuario
        print("Datos incorrectos, por favor vuelva a ingresar sus datos")
        contrasenia=input("Ingrese su contraseña: ")
    return True, usuario

def menu():
    print("""
    ****** Bienvenid@ al menu de Medicorp ******
    Ingrese a una de las siguientes opciones con el número asignado:
    1 para alta de paciente,
    2 para alta de turno,
    3 para modificar datos del paciente,
    4 para baja de paciente,
    5 para baja de turno,
    6 para listar turnos según dia y mes,
    7 para listar pacientes,
    8 para buscar turno según DNI,
    9 para cargar datos de prueba,
    10 para buscar paciente,
    11 para listar pacientes segun edad ingresada,
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
        pacientes = open('datos_pacientes.txt','r')
    except IOError:
        print("No se pudo leer el archivo")
    else:
        linea = pacientes.readline()
        while linea != '':	
            linea = linea.rstrip()
            paciente = linea.split(';')
            dni = paciente[0]
            if dni == modificar_datos_dni:
                pacientes = open('datos_pacientes.txt','w')
                apellido = input("Ingrese apellido del paciente: ")
                nombre = input("Ingrese nombre del paciente: ")
                edad = int(input('Ingrese edad del paciente: '))
                paciente= [str(dni),apellido.capitalize(), nombre.capitalize(), str(edad)]
                paciente = ';'.join(paciente)
                pacientes.write(paciente)
                print(f'Paciente con DNI {dni} modificado con exito.')
            linea = pacientes.readline()

def pacientes_a_listas():
    """
    Leemos el archivo y pasamos los datos de los pacientes a listas.
    """
    try:
        arch=open("datos_pacientes.txt",'r')
    except IOError:
        print("No se pudo leer el archivo")
    except:
        print("Ocurrió un error inesperado")
    else:
        lista_dni=[]
        lista_nombre=[]
        lista_apellido=[]
        lista_edad=[]
        linea=arch.readline()
        while linea != "":
            linea=linea.rstrip()
            pacientes=linea.split(";")
            lista_dni.append(pacientes[0])
            lista_apellido.append(pacientes[1])
            lista_nombre.append(pacientes[2])
            lista_edad.append(pacientes[3])
            linea=arch.readline()
    return lista_dni,lista_apellido,lista_nombre,lista_edad

def ordenar_pacientes(lista_dni,lista_apellido,lista_nombre,lista_edad):
    """
    Se ordena las listas de la pacientes según los apellidos.
    Se utiliza el metodo de incersión.
    """
    for i in range(1,len(lista_apellido)):
        apellido_aux=lista_apellido[i]
        nombre_aux=lista_nombre[i]
        dni_aux=lista_dni[i]
        edad_aux=lista_edad[i]
        j=i
        while j>0 and lista_apellido[j-1]>apellido_aux:
            lista_apellido[j]=lista_apellido[j-1]
            lista_nombre[j]=lista_nombre[j-1]
            lista_dni[j]=lista_dni[j-1]
            lista_edad[j]=lista_edad[j-1]
            j=j-1
        lista_apellido[j]=apellido_aux
        lista_nombre[j]=nombre_aux
        lista_dni[j]=dni_aux
        lista_edad[j]=edad_aux


def grabar_pacientes(lista_dni,lista_apellido,lista_nombre,lista_edad):
    """
    Se graban las listas de los datos de los pacientes en el archivo.
    """
    try:
        arch=open("datos_pacientes.txt","w")
    except IOError:
        print("No se pudo leer el archivo")
    except:
        print("Ocurrió un error inesperado")
    else:
        for i in range(len(lista_dni)):
            paciente=[lista_dni[i],lista_apellido[i],lista_nombre[i],lista_edad[i]]
            paciente=";".join(paciente)
            arch.write(paciente+"\n")

def listar_pacientes():
    """
    Imprime en pantalla el archivo de pacientes dados de alta.
    """
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
            print(f'DNI:{dni:08d}   APELLIDO: {apellido:<15s}' + 
            f'NOMBRE: {nombre:<15s} EDAD: {edad:02d}')
            linea = pacientes.readline()
      
def cargar_pacientes_dni():
    """
    Se leen el archivo que contiene todos los pacientes dados de alta.
    Se carga en una lista los DNI de los pacientes.
    Se retorna la lista.
    """
    try:
        pacientes = open('datos_pacientes.txt','r')
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

def validar_dni(dni):
    while dni.isnumeric() == False or int(dni)>99999999 or int(dni)<1000000:
        print("DNI ingresado es inválido.")
        dni = input('Ingrese el DNI del paciente: ')
    return dni

def alta_paciente():
    lista_dni = cargar_pacientes_dni()
    try:
        pacientes = open('datos_pacientes.txt','a')
    except FileNotFoundError:
        print("El archivo de paciente no se encuentra.")
    except:
        print("Error inesperado")
    else:
        while True:
            try:
                dni = input('Ingrese el DNI del paciente: ')
                dni = validar_dni(dni)
                while int(dni) in lista_dni:
                    dni = input('ERROR: el dni ingresado ya existe. Ingrese el DNI del paciente: ')
                    dni = validar_dni(dni)
            except TypeError:
                print ('Error de tipo')
            except:
                print ('Error inesperado')
            else:
                apellido = input('Ingrese el apellido del paciente: ')
                while apellido.isalpha()==False:
                    print("El apellido del paciente es inválido.")
                    apellido = input('Ingrese el apellido del paciente: ')
                nombre = input('Ingrese el nombre del paciente: ')
                while nombre.isalpha()==False:
                    print("El nombre del paciente es inválido.")
                    nombre = input('Ingrese el apellido del paciente: ')
                edad =input('Ingrese edad del paciente: ')
                while edad.isnumeric()!=True or int(edad)<18:
                    if edad.isnumeric()!=True:
                        print("Se permiten solo numeros.")
                    else:
                        print("Debe ser mayor de edad.")
                    edad =input('Ingrese edad del paciente: ')
                paciente= [str(dni),apellido.capitalize(), nombre.capitalize(), edad]
                paciente = ';'.join(paciente)
                pacientes.write(paciente + '\n')
                print("Los datos del nuevo paciente se agregaron existosamente.")
                break

def baja_paciente(lista_dni,lista_apellido,lista_nombre,lista_edad):
    dni=input("""Has elegido dar de baja un paciente. 
    Ingrese el DNI del paciente a dar de baja: """)
    veces=lista_dni.count(dni)
    if veces==0:
        print("El paciente no fue dado de alta.")
    else:
        pos=lista_dni.index(dni)
        lista_dni.pop(pos)
        lista_apellido.pop(pos)
        lista_nombre.pop(pos)
        lista_edad.pop(pos)
        print("Paciente dado de baja correctamente.")

def run():
    pass

if __name__ == '__main__':
    run()