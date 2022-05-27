from json.tool import main
from random import randint
from tkinter import Menu

##################################################################################
# numero_maquina function which generated a random number and validate if the user can guess the random number
def numero_maquina():
    print('Genial!! en esta modalidad debes adivinar un numero aleatorio generado por la maquina')
    print(' ')
    numero_rango = randint(1,100)
    numero_jugador = int(input('Adivina un numero entre el 1 y el ' + str(numero_rango) + ': '))
    numero_maquina = randint(1,numero_rango)
    #print(str(numero_maquina))
    while numero_jugador != numero_maquina:
        if numero_jugador < numero_maquina:
            print('Ups lo siento intenta de nuevo con numero mas grande: ')
        else:
            print('Ups lo siento intenta de nuevo con numero mas pequeño: ')
        numero_jugador = int(input())

    print('Felicidades adivinaste el numero')


##################################################################################
# numero_maquina function which generated a random number and guess the random number enter by the user
def numero_usuario():
    print('Genial!! en esta modalidad debes ingresar un numero y la maquina lo va a adivinar')
    print(' ')
    numero_jugador = int(input('Ingresa un numero cualquiera: '))
    numero_maquina = randint(1,numero_jugador)
    contador = 1
    #print(str(numero_maquina))
    while numero_jugador != numero_maquina:
        contador += 1
        numero_maquina = randint(1,numero_jugador)

    print('El numero adivinado por la maquina es ' + str(numero_maquina) + ' y la maquina realizo ' + str(contador) +  ' intentos por adivinar el numero')
    

##################################################################################
# tipo_juego function which defined the type of game according to option choised
def tipo_juego(modo_juego):

    if modo_juego == 1:
        numero_maquina()  
    elif modo_juego == 2:
        numero_usuario()
    else:
        print('Opción invalida')

#modo_juego

##################################################################################
# main function
def main():
    
    menu = """
    Hola bienvenido al juego de los numeros, las reglas son muy simples
    tienes 2 opciones:

    1. Adivinar un numero aleatorio generado por la maquina.
    2. Ingresar un numero cualquiera, y la maquina debe adivinarlo

    Selecciona la modalidad que deseas.

    """
    modo_juego = int(input(menu))
    tipo_juego(modo_juego)


if __name__=='__main__':
    main()