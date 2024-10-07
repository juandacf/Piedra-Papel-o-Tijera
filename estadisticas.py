import os
def generalStatistics(mainDict):
    os.system('clear')
    threeBestGeneralPlayers(mainDict)
    worstPlayer(mainDict)
    ThreelosersAgainstMachine(mainDict)
    winnersAgainsMachine(mainDict)

    input('Cuando oprima enter, volverá al menú principal')

def threeBestGeneralPlayers(mainDict):
    players ={}
    scores = []
    bestPlayers= []
    for k,v in mainDict.items():
        playername= v.get('name')
        totalPoints= v.get('statistics')[0]
        players.update({playername:totalPoints})
        scores.append(totalPoints)
    for i in range(0,3):
        bestPlayers.append(scores.pop(scores.index(max(scores))))
        
    rank1=bestPlayers[0]
    rank2=bestPlayers[1]
    rank3=bestPlayers[2]

    for k,v in mainDict.items():
        if v.get('statistics')[0]==rank1:
            indexRank1= k
        if v.get('statistics')[0]==rank2:
            indexRank2= k
        if v.get('statistics')[0]==rank3:
            indexRank3=k
    
    print(f"""
1. El jugador con rank 1,en base a los puntos totales, es {mainDict.get(indexRank1).get('nickname')} con un puntaje de {mainDict.get(indexRank1).get('statistics')[0]}
2. El jugador con rank 2, en base a los puntos totales, es {mainDict.get(indexRank2).get('nickname')} con un puntaje de {mainDict.get(indexRank2).get('statistics')[0]}
3.El jugador con rank 3, es {mainDict.get(indexRank3).get('nickname')} con un puntaje de {mainDict.get(indexRank3).get('statistics')[0]}
""")
     
        
def worstPlayer(mainDict):
    players = {}
    scores = []
    for k,v in mainDict.items():
        playerNickname= v.get('nickname')
        playerScore = v.get('statistics')[0]
        players.update({playerNickname:playerScore})
        scores.append(playerScore)
    worstScore=min(scores)
    for k,v in players.items():
        if v==worstScore:
            worstNickname= k
    
    print(f'El jugador con la peor puntuacion fue {worstNickname} con {worstScore} puntos')

def ThreelosersAgainstMachine(mainDict):
    players ={}
    scores = []
    worstPlayers= []
    for k,v in mainDict.items():
        playername= v.get('nickname')
        totalLosses= v.get('statistics')[2]
        players.update({playername:totalLosses})
        scores.append(totalLosses)
    for i in range(0,3):
        worstPlayers.append(scores.pop(scores.index(max(scores))))
        
    rank1=worstPlayers[0]
    rank2=worstPlayers[1]
    rank3=worstPlayers[2]

    for k,v in players.items():
        if v==rank1:
            nameRank1= k
        if v==rank2:
            nameRank2= k
        if v==rank3:
            nameRank3=k
    
    print(f"""
1. El primer jugador con mas perdidas contra la máquina es {nameRank1} con {rank1} derrotas.
2. El segundo jugador con mas perdidas contra la máquina es {nameRank2} con {rank2} derrotas.
3.El tercer jugador mas perdidas contra la máquina es {nameRank3} con {rank3} derrotas.
""")

def winnersAgainsMachine (mainDict):
    totalPLayers= len(mainDict)-1
    winnersMachine= 0

    for k,v in mainDict.items():
        if v.get('name')=='AI':
            pass
        else:
            if v.get('statistics')[1]>0:
                winnersMachine+=1

    print(f'{winnersMachine} de {totalPLayers} le han ganado a la máquina.')

