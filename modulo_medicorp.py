import os; clear = lambda: os.system('cls'); clear()
import sys

class max_attempts_reached(Exception):
    pass

def load_login_info():
    user_names = []
    user_passwords = []
    with open('user_names.txt', 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        user_names.append(lines[i].rstrip('\n').split(','))
    f.close()
    with open('user_passwords.txt', 'r') as f:
        lines = f.readlines()
    for i in range(len(lines)):
        user_passwords.append(lines[i].rstrip('\n').split(','))
    f.close()
    return user_names, user_passwords
    
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
            menu_selection = int(input())
            assert (menu_selection>= 0 and menu_selection <=9), "Opción ingresada incorrecta"
        except AssertionError as error:
            clear()
            print(error)
        else:
            break
    return menu_selection

def login(load):
# Se chequea que el usuario existe.
# Se compara la contraseña ingresada con la guardada.
# Si todo es correcto devuelve el usuario.tg 
    print("***** Bienvenid@ a Medicorp *****")
    user_names, user_passwords = load
    attempts = 3
    while True:
        try:
            if attempts <= 0:
                raise max_attempts_reached
            attempts -= 1
            user = input("Ingrese su usuario: ")
            password = input("Ingrese su contraseña: ")       
            assert ([user] in user_names), "El usuario no existe."
            password_index = user_names.index([user])
            assert ([password] == user_passwords[password_index]), "La contraseña es incorrecta."
        except AssertionError as error:
            clear()
            print(error) 
        except max_attempts_reached:
            clear()
            print("Se detectó 3 intentos fallidos.")
            break
        except:
            clear()
            print("Error inesperado:", sys.exc_info()[0])
            raise
        else:
            clear()
            return user 

def run():
    pass

if __name__ == '__main__':
    run()