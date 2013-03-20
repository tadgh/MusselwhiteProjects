import os
import pickle
from threading import *
import time
import sys
import datetime

rootPath = "\\\\muspfl01\Group\Public Access\Camp\Today's Menu"
filePath = os.path.join("pickledFoods")
extantItems = []
recentlyEmailed = False
now = datetime.datetime.now()
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
                elif "~" not in fileOrFolder and ".docx" in fileOrFolder and str(now.day) in fileOrFolder:
                    print("Emailed!")
                    os.system("ruby " + "spammer.rb " + "\""+pathName + "\"") #worlds ugliest and laziest workaround. DONT JUDGE ME
                    x = open(os.path.join("pickledFoods"), "wb")
                    pickle.dump(extantItems, x)
                    sys.exit()

def getOldList():
    pickledFile = open(os.path.join("pickledFoods"), "rb")
    returnValue =  pickle.load(pickledFile)
    print("GOT OLD LIST")
    pickledFile.close()
    return returnValue

def runIt():
    index = 0
    while index < 24:
        #extantItems = []
        extantItems = getOldList()
        runThroughDir(extantItems)
        print(extantItems)
        x = open(os.path.join("pickledFoods"), "wb")
        pickle.dump(extantItems, x)
        x.close()
        time.sleep(300)

if __name__ == "__main__":
    runIt()






