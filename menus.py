
import os

def validateUser():
    os.system('clear')
    optionChosen = input("""
                         
PIEDRA🪨, PAPEL📃 O TIJERA 8<
Por favor, ingrese la mejor opción:
1. Registrarme como usuario nuevo. 
2. Jugar (2 jugadores)
3. Jugar (1 vs IA)
4. Ver estadísticas notables
5. Salir del programa. 
""")
    match optionChosen:
        case 1:
            pass
        case 2:
            pass
        case 3:
            pass
        case 4:
            pass
        case 5:
            input('Gracias por participar. Una vez oprima enter, el programa habrà terminado.')
        case _:
            input("La opciòn ingresada no es correcta. Cuando oprima enter, volverá al menú inicial.")
            validateUser()