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