def generalStatistics(mainDict):
    threeBestGeneralPlayers(mainDict)
    worstPlayer(mainDict)
    ThreelosersAgainstMachine(mainDict)
    winnersAgainsMachine(mainDict)

def threeBestGeneralPlayers(mainDict):
    players ={}
    scores = []
    for k,v in mainDict.items():
        playername= v.get('name')
        totalPoints= v.get('statistics')[0]
        players.update({playername:totalPoints})
        scores.append[totalPoints]
        scores.sort()


def worstPlayer(mainDict):
    pass

def ThreelosersAgainstMachine(mainDict):
    pass

def winnersAgainsMachine (mainDict):
    pass

