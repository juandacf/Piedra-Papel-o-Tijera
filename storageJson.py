import json
import os
dataBasePath = 'data/storage.json'

def newFile():
    with open (dataBasePath, "w") as wf:
        json.dump({}, wf, indent=4)

def readFile():
    with open(dataBasePath, "r") as rf:
        return json.load(rf)
        

def addData(dictName):
    with open (dataBasePath, "w") as frw:
        json.dump(dictName,frw, indent=4)

def checkFile():
    if (os.path.isfile(dataBasePath)):
        pass
    else:
        newFile() 