import os; clear = lambda: os.system('cls'); clear()
import sys
from modulo_medicorp import *


def run():
    print("MEDICORP SOFTWARE SOLUTIONS")
    lista_usuarios=("medicorp","admin")
    lista_contrasenias=("1234","4321abc")
    permitido,user=login(lista_usuarios,lista_contrasenias)
    clear()
    if permitido == True:
        print(f'El usuario {user} ha ingresado correctamente.')
    else:
        return print("Los datos de login son incorrectos")
    while True:
        clear()
        menu_selection = menu()
        # Se ejecutan las distintas funciones selecionadas.
        if menu_selection == 1:
            clear()
            alta_paciente()
        if menu_selection == 2:
            pass
        if menu_selection == 3:
            clear()
            dni = int(input("Ingrese el DNI del paciente a modificar sus datos: "))
            lista_dni = cargar_pacientes_dni()
            if dni in lista_dni :
                modificar_paciente(dni)
            else:
                print("El paciente no existe en la base de datos")
                exit = input("Presione enter para continuar al menu principal")
        if menu_selection == 4:
            pass
        if menu_selection == 5:
            pass
        if menu_selection == 6:
            pass
        if menu_selection == 7:
            clear()
            d,a,n,e = pacientes_a_listas()
            ordenar_pacientes(d,a,n,e)
            grabar_pacientes(d,a,n,e)
            listar_pacientes()
        if menu_selection == 8:
            pass
        if menu_selection == 9:
            pass
        if menu_selection == 0:
            break
            
    clear()

if __name__ == '__main__':
    run()
    print("Gracias por utilizar MEDICORP SOFTWARE SOLUTIONS")