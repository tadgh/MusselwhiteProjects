import os
import pickle
from threading import *
import time

rootPath = "\\\\muspfl01\Group\Public Access\Camp\Today's Menu"
filePath = os.path.join("pickledFoods")
extantItems = []
recentlyEmailed = False

def runThroughDir( extantItems, path = rootPath):
    for fileOrFolder in os.listdir(path):
        pathName = os.path.join(path, fileOrFolder)
        if os.path.isdir(pathName):
            runThroughDir(extantItems, pathName)
        else:
            if fileOrFolder in extantItems:
                pass
            elif fileOrFolder not in extantItems:
                print("FOUND A NEW FILE!! New item: " + pathName)
                extantItems.append(fileOrFolder)
                if "~" in fileOrFolder:
                    print("oops just a temporary file, never mind!")
                elif "~" not in fileOrFolder:
                    print("Emailed!")
                    #os.system("ruby " + "spammer.rb " + "\""+pathName + "\"") #worlds ugliest and laziest workaround. DONT JUDGE ME

def getOldList():
    pickledFile = open(os.path.join("pickledFoods"), "rb")
    returnValue =  pickle.load(pickledFile)
    print("GOT OLD LIST")
    pickledFile.close()
    return returnValue

def runIt():
    while not recentlyEmailed:
        #extantItems = []
        extantItems = getOldList()
        runThroughDir(extantItems)
        print(extantItems)
        x = open(os.path.join("pickledFoods"), "wb")
        pickle.dump(extantItems, x)
        x.close()
        time.sleep(300)

if __name__ == "__main__":
    scanTimer = Timer(3.0, runIt)
    scanTimer.start()






