
import os
import validateUser as vu
import storageJson as sj
import game as gm
import estadisticas as s

mainDictionary ={}
sj.checkFile()
mainDictionary= sj.readFile()


def mainMenu(mainDict):
    os.system('clear')
    try:
        optionChosen = int(input("""
                            
    PIEDRA🪨, PAPEL📃 O TIJERA 8<
    Por favor, ingrese la mejor opción:
    1. Registrarme como usuario nuevo. 
    2. Jugar (2 jugadores)
    3. Jugar (1 vs IA)
    4. Ver estadísticas notables
    5. Salir del programa. 
    """))
    except:
        input('La opción ingresada no es válida. Cuando oprima enter, será llevado al menú principal')
        mainMenu(mainDict)
    match optionChosen:
        case 1:
            os.system('clear')
            vu.signUp(mainDict)
            sj.addData(mainDict)
            mainMenu(mainDict)
        case 2:
            os.system('clear')
            gm.twoPlayerGame(mainDict)
            sj.addData(mainDict)
            mainMenu(mainDict)
        case 3:
            os.system('clear')
            gm.onePlayerGame(mainDict)
            sj.addData(mainDict)
            mainMenu(mainDict)
        case 4:
            s.generalStatistics(mainDict)
            mainMenu(mainDict)
        case 5:
            os.system('clear')
            input('Gracias por participar. Una vez oprima enter, el programa habrà terminado.')
        case _:
            input("La opciòn ingresada no es correcta. Cuando oprima enter, volverá al menú inicial.")
            mainMenu(mainDict)
        
mainMenu(mainDictionary)