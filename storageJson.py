import json
import os

dataBasePath = 'data/storageDictionary.json' #Al momento de ejeucuón del programa, revisar que se esté en la carpeta Proyecto_PythonCaballeroJuan

def newFile(fileName):
    with open (dataBasePath, "w") as wf:
        json.dump(fileName, wf, indent=4)

def readFile():
    with open(dataBasePath, "r") as rf:
        return json.load(rf)
        

def addData(dictName):
    with open (dataBasePath, "w") as frw:
        json.dump(dictName,frw, indent=4)

def checkFile(dictName):
    if (os.path.isfile(dataBasePath)):
        pass
    else:
        newFile(dictName) 