import validateUser as vu
import os 
import random
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
        if v.get('nickname')==second:
            indexpl2=k


    while(switchGame==True): #validar el ingreso de strings para que no salga error 

        optionpl1= int(input(f'Por favor,{first}, ingrese 1 para escoger piedra🪨. Ingrese 2 para papel📃. Ingrese 3 para tijera8<: '))
        optionpl2= int(input(f'Por favor,{second}, ingrese 1 para escoger piedra🪨. Ingrese 2 para papel📃. Ingrese 3 para tijera8<: '))
        if(optionpl1<4 and optionpl1>0) or (optionpl2<4 and optionpl2>0):
            if (optionpl1==1 and optionpl2==1) or (optionpl1==2 and optionpl2==2) or (optionpl1==3 and optionpl2==3):
                input('Esta ronda fue un empate. Presione enter para ir a la siguiente ronda')
            elif(optionpl1==2 and optionpl2==1) or (optionpl1==3 and optionpl2==2) or (optionpl1==1 and optionpl2==3): #partida ganada pl1
                if(mainDict.get(indexpl2).get('statistics')[4]==True):
                    mainDict.get(indexpl2).get('statistics')[4]=False
                    print(f'el jugador {second} ha perdido esta ronda. Sin embargo,ha perdido su escudo y la derrota no contará.')
                else:
                    consecutivespl1+=1
                    consecutivespl2=0
                    print(f'{first} lleva {consecutivespl1} partidas ganadas. {second} ahora tiene 0')
            elif (optionpl2==2 and optionpl1==1) or (optionpl2==3 and optionpl1==2) or (optionpl2==1 and optionpl1==3): #partida ganada pl2
                if(mainDict.get(indexpl1).get('statistics')[4]==True):
                    mainDict.get(indexpl1).get('statistics')[4]=False
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
    os.system('clear')
    print(f'{player} jugará contra la IA ')
    consecutivespl1=0
    consecutivesIA=0
    indexpl1=0
    indexpIA=0
    switchGameM= True

    for k,v in mainDict.items(): #buscar indice del jugador 1
        if v.get('nickname')==player:
            indexpl1=k

    while(switchGameM==True):
        optionpl1= int(input(f'Por favor,{player}, ingrese 1 para escoger piedra🪨. Ingrese 2 para papel📃. Ingrese 3 para tijera8<: '))
        optionIA= random.randint(1,3)

        if(optionpl1<4 and optionpl1>0) or (optionIA<4 and optionIA>0):
            if (optionpl1==1 and optionIA==1) or (optionpl1==2 and optionIA==2) or (optionpl1==3 and optionIA==3):
                input('Esta ronda fue un empate. Presione enter para ir a la siguiente ronda')
            elif(optionpl1==2 and optionIA==1) or (optionpl1==3 and optionIA==2) or (optionpl1==1 and optionIA==3): #partida ganada pl1
                if(mainDict.get(indexpIA).get('statistics')[3]==True):
                    mainDict.get(indexpIA).get('statistics')[3]=False
                    print(f'La IA ha perdido esta ronda. Sin embargo,ha perdido su escudo y la derrota no contará.')
                else:
                    consecutivespl1+=1
                    consecutivesIA=0
                    print(f'{player} lleva {consecutivespl1} rondas  ganadas. IA ahora tiene 0')
            elif (optionIA==2 and optionpl1==1) or (optionIA==3 and optionpl1==2) or (optionIA==1 and optionpl1==3): #partida ganada IA
                if(mainDict.get(indexpl1).get('statistics')[4]==True):
                    mainDict.get(indexpl1).get('statistics')[4]=False
                    print(f'El jugador {player} ha perdido esta ronda. Sin embargo,ha perdido su escudo y la derrota no contará.')
                else:
                    consecutivesIA+=1
                    consecutivespl1=0
                print(f' IA lleva {consecutivesIA} rondas ganadas. {player} ahora tiene 0')
        else:
            print("Por favor, ingrese un valor adecuado:")

        if (consecutivespl1==3) or (consecutivesIA==3):
            switchGameM= False

    if(consecutivespl1==3):
        mainDict.get(indexpl1).get('statistics')[3]+=1 #+1 victoria consecutiva al jugador
        if mainDict.get(indexpl1).get('statistics')[3]==2:
            mainDict.get(indexpl1).get('statistics')[4]=True #Si el jugador tiene dos victorias consecutivas, gana escudo
            print(f'Por haber ganado dos partidas consecutivas, el jugador{player} se ha ganado un escudo.')
        mainDict.get(indexpl1).get('statistics')[0]+=2 #+2 puntos totales
        mainDict.get(indexpl1).get('statistics')[1]+=1 #+1 victoria contra la IA 
        mainDict.get(indexpIA).get('statistics')[2]=0 #Las victorias consecutivas de la máquina se vuelven 0
        input(f'El ganador de la partida fue el {player}. Presione enter para volver al menú principal')
    if (consecutivesIA==3):
        mainDict.get(indexpIA).get('statistics')[2]+=1 # Se le agrega una victoria consecutiva a la IA
        if mainDict.get(indexpIA).get('statistics')[2]==2: 
            mainDict.get(indexpIA).get('statistics')[3]=True #Si la IA tiene dos victorias consecutivas, se le agrega un esucdo
            print(f'Por haber ganado dos partidas consecutivas, la IA se ha ganado un escudo.')
        mainDict.get(indexpIA).get('statistics')[0]+=2 #se le agrega dos puntos totales a la IA 
        mainDict.get(indexpl1).get('statistics')[3]=0 #Las victorias consecutivas de el jugador se vuelven 0
        mainDict.get(indexpl1).get('statistics')[2]+=1 # Se le suma una derrota contra la máquina al jugador
        input(f'El ganador de la partida fue la IA. Presione enter para volver al menú principal')

    

def onePlayerGame(mainDict:dict):
    os.system('clear')
    print('Por favor, ingrese los datos del jugador para jugar contra la máquina')
    playerValidation= vu.logIn(mainDict)
    
    if (type(playerValidation)==str):
        playerVsMachine(playerValidation, mainDict)
    else:
        input("La información no pudo ser verificada. Cuando oprima enter,será llevado al  menú principal")
        






   