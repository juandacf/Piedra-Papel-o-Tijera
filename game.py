import validateUser as vu
import os 

def actualGame2(first,second,mainDict):
    os.system('clear')
    print(f'{first} será el primer jugador. {second} será el segundo')
    consecutivespl1=0
    consecutivespl2=0
    while(consecutivespl1<3 or consecutivespl2<3): #validar el ingreso de strings para que no salga error 

        optionpl1= int(input(f'Por favor,{first}, ingrese 1 para escoger piedra🪨. Ingrese 2 para papel📃. Ingrese 3 para tijera8<: '))
        optionpl2= int(input(f'Por favor,{second}, ingrese 1 para escoger piedra🪨. Ingrese 2 para papel📃. Ingrese 3 para tijera8<: '))
        if(optionpl1<4 and optionpl1>0) or (optionpl2<4 and optionpl2>0):
            if (optionpl1==1 and optionpl2==1) or (optionpl1==2 and optionpl2==2) or (optionpl1==3 and optionpl2==3):
                input('Esta ronda fue un empate. Presione enter para ir a la siguiente partida')
            elif(optionpl1==2 and optionpl2==1) or (optionpl1==3 and optionpl2==2) or (optionpl1==1 and optionpl2==3): #partida ganada pl1
                consecutivespl1+=1
                consecutivespl2=0
                print(f'{first} lleva {consecutivespl1} partidas ganadas. {second} ahora tiene 0')
            elif (optionpl2==2 and optionpl1==1) or (optionpl2==3 and optionpl1==2) or (optionpl2==1 and optionpl1==3): #partida ganada pl2
                consecutivespl2+=1
                consecutivespl1=0
                print(f'{second} lleva {consecutivespl1} partidas ganadas. {first} ahora tiene 0')
        else:
            print("Por favor, ingrese un valor adecuado:")
    
    if(consecutivespl1==3):
        print(f'El ganador fue el {first}')
    elif (consecutivespl2==3):
        print(f'El ganador fue el {second}')

def twoPlayerGame(mainDict:dict):
    os.system('clear')
    print("Por favor, ingrese los datos del primer jugador")
    firstPlayer=vu.logIn(mainDict)
    os.system('clear')
    print("Por favor, ingrese los datos del segundo jugador")
    secondPlayer=vu.logIn(mainDict)

    if(type(firstPlayer)==str and type(secondPlayer)==str):
        actualGame2(firstPlayer,secondPlayer,mainDict)
    else:
        input("La información no pudo ser verificada. Cuando oprima enter,será llevado al  menú principal")





   