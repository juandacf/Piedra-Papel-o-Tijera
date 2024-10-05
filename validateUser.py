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
                'nickname': 'AI',
                'statistics':{
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
                'statistics': {
                    'totalScore': 0,
                    'scoreMachine':0,
                    'lossesAgainstMachine':0,
                    'shield':False,
                    'consecutiveMatches':0
                }
            
            }
            mainDict.update({int(len(mainDict)):playerConstructor})
        else:
            input('El nickname elegido ya fue previamente escogido. Escoja otro.')
        signUpRepetition= bool(input("Si desea agregar algún otro nombre, presione un caracter y enter. Si no, solo oprima enter."))

def logIn(mainDict:dict):

    completeName = str(input("Por favor, ingrese su primer nombre y primer apellido sin espacios para identificarse")).lower()
    nickName = str(input("Por favor, ingrese el nickname para identificarse ")).lower()
    validateSwitch= False

    for k,v in mainDict.items():
        if v.get('name')==completeName:
            if v.get('nickname')==nickName:
                validateSwitch= True
    
    if(validateSwitch==True):
        return True
    else:
        return False
    
def validateTwoPlayers(mainDict:dict):
    os.system('clear')
    print('Ingrese los datos de validaciòn del primer usuario')
    user1validation = logIn(mainDict)
    os.system('clear')
    print('Ingrese los datos de validaciòn del segundo usuario')
    user2validation =logIn(mainDict)

    if (user1validation==True and user2validation==True):
        return True
    else:
        return False
    
   

    






   
    









