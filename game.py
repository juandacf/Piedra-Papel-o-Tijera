import validateUser as vu
import os 

def actualGame2(first,second,mainDict):
    os.system('clear')
    print(f'{first} será el primer jugador. {second} será el segundo')
    consecutivespl1=0
    consecutivespl2=0
    indexpl1=0
    indexpl2=0
    switchGame= True


    for k,v in mainDict.items(): #buscar indice del jugador 1
        if v.get('nickname')==first:
            indexpl1=k
    
    for k,v in mainDict.items(): #buscar indice del jugador 2
        if v.get('nickname')==first:
            indexpl2=k


    while(switchGame==True): #validar el ingreso de strings para que no salga error 

        optionpl1= int(input(f'Por favor,{first}, ingrese 1 para escoger piedra🪨. Ingrese 2 para papel📃. Ingrese 3 para tijera8<: '))
        optionpl2= int(input(f'Por favor,{second}, ingrese 1 para escoger piedra🪨. Ingrese 2 para papel📃. Ingrese 3 para tijera8<: '))
        if(optionpl1<4 and optionpl1>0) or (optionpl2<4 and optionpl2>0):
            if (optionpl1==1 and optionpl2==1) or (optionpl1==2 and optionpl2==2) or (optionpl1==3 and optionpl2==3):
                input('Esta ronda fue un empate. Presione enter para ir a la siguiente partida')
            elif(optionpl1==2 and optionpl2==1) or (optionpl1==3 and optionpl2==2) or (optionpl1==1 and optionpl2==3): #partida ganada pl1
                if(mainDict.get(indexpl2).get('statistics')[3]==True):
                    mainDict.get(indexpl2).get('statistics')[3]=False
                    print(f'el jugador {second} ha perdido esta ronda. Sin embargo,ha perdido su escudo y la derrota no contará.')
                else:
                    consecutivespl1+=1
                    consecutivespl2=0
                    print(f'{first} lleva {consecutivespl1} partidas ganadas. {second} ahora tiene 0')
            elif (optionpl2==2 and optionpl1==1) or (optionpl2==3 and optionpl1==2) or (optionpl2==1 and optionpl1==3): #partida ganada pl2
                if(mainDict.get(indexpl1).get('statistics')[3]==True):
                    mainDict.get(indexpl1).get('statistics')[3]=False
                else:
                    consecutivespl2+=1
                    consecutivespl1=0
                print(f'{second} lleva {consecutivespl2} partidas ganadas. {first} ahora tiene 0')
        else:
            print("Por favor, ingrese un valor adecuado:")

        if (consecutivespl1==3) or (consecutivespl2==3):
            switchGame= False

    if(consecutivespl1==3):
        mainDict.get(indexpl1).get('statistics')[3]+=1
        if mainDict.get(indexpl1).get('statistics')[3]==2:
            mainDict.get(indexpl1).get('statistics')[4]=True
            print(f'Por haber ganado dos partidas consecutivas, el jugador{first} se ha ganado un escudo.')
        mainDict.get(indexpl1).get('statistics')[0]+=2
        mainDict.get(indexpl2).get('statistics')[3]=0
        input(f'El ganador de la partida fue el {first}. Presione enter para volver al menú principal')
    if (consecutivespl2==3):
        mainDict.get(indexpl2).get('statistics')[3]+=1
        if mainDict.get(indexpl2).get('statistics')[3]==2:
            mainDict.get(indexpl2).get('statistics')[4]=True
            print(f'Por haber ganado dos partidas consecutivas, el jugador{second} se ha ganado un escudo.')
        mainDict.get(indexpl2).get('statistics')[0]+=2
        mainDict.get(indexpl1).get('statistics')[3]=0
        input(f'El ganador de la partida fue el {second}. Presione enter para volver al menú principal')

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

def playerVsMachine(player, mainDict:dict):
    pass

def onePlayerGame(mainDict:dict):
    os.system('clear')
    print('Por favor, ingrese los datos del jugador para jugar contra la máquina')
    playerValidation= vu.logIn(mainDict)
    
    if (playerValidation==str):
        playerVsMachine(playerValidation, mainDict)
    else:
        input("La información no pudo ser verificada. Cuando oprima enter,será llevado al  menú principal")






   