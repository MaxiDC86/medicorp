import os; clear = lambda: os.system('cls'); clear()
import sys
from modulo_medicorp import *



def run():
    user = login(load_login_info())
    print(f'El usuario {user} ha ingresado correctamente.')
    menu()
    clear()

if __name__ == '__main__':
    run()