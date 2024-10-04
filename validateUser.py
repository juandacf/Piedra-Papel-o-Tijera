import os 
def signUp (mainDict):
    signUpRepetition=True
    while (signUpRepetition):
        os.system('clear')
        print('Para llevar a cabo el registro, digite la siguiente información: ')
        completeName = str(input("Por favor, ingrese su primer nombre y primer apellido sin espacios.")).lower()
        nickName = str(input("Por favor, ingrese el nickname para identificarse en el juego.")).lower()
        signUpPermission = True

        if(len(mainDict)>0):
            for i in range (1,len(mainDict)):
                if(nickName==mainDict[i]['nickname']):
                    signUpPermission=False


        if (len(mainDict)==0):
            machineConstructor = {
                'name':'AI',
                'machineStatistics': {
                    'totalScore': 0,
                    'losses':0,
                    'consecutiveMatches':0,
                    'shield':False,
                }
            }
            mainDict.update({0:machineConstructor})
        
        if(signUpPermission==True):
            playerConstructor = {
                'name': completeName,
                'nickname': nickName,
                'playerStatistics': {
                    'totalScore': 0,
                    'scoreMachine':0,
                    'lossesAgainstMachine':0,
                    'shield':False,
                    'consecutiveMatches':0
                }
            
            }
            mainDict.update({len(mainDict):playerConstructor})
        else:
            input('El nickname elegido ya fue previamente escogido. Escoja otro.')
        signUpRepetition= bool(input("Si desea agregar algún otro nombre, presione un caracter y enter. Si no, solo oprima enter."))

def userLogin (mainDict):
    userLoginRepetition = False
    while (userLoginRepetition==False):
        completeName = str(input("Por favor, ingrese su nombre completo sin espacios y en minúsculas")).lower()
        nickName = str(input("Por favor, ingrese su nickname")).lower()
        nameSwitch = False
        nickNameSwitch =False

    for i in range(1, len(mainDict)+1):
        if (completeName==mainDict[i]['name']):
            nameSwitch=True
            nameIndex = i
            if (nickName==mainDict[nameIndex]['nickname']):
                nickNameSwitch=True
    
    if(nameSwitch==True and nickNameSwitch):
        return True
    else:
        return False





