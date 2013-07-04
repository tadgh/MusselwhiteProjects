import os
import pickle
from threading import *
import time
import sys
import datetime

root_path = "\\\\10.19.110.117\Group\Public Access\Camp\Today's Menu"
file_path = os.path.join("pickledFoods")
extant_items = []
recently_emailed = False
now = datetime.datetime.now()


def run_through_dir(extant_items, path=root_path):
    for file_or_folder in os.listdir(path):
        pathName = os.path.join(path, file_or_folder)
        if os.path.isdir(pathName):
            run_through_dir(extant_items, pathName)
        else:
            if file_or_folder in extant_items:
                pass
            elif file_or_folder not in extant_items:
                print("FOUND A NEW FILE!! New item: " + pathName)
                extant_items.append(file_or_folder)
                if "~" in file_or_folder:
                    print("oops just a temporary file, never mind!")
                elif "~" not in file_or_folder and ".docx" in file_or_folder and str(now.day) in file_or_folder:
                    print("Emailed!")
                    os.system("ruby " + "spammer.rb " + "\"" + pathName + "\"")  # worlds ugliest and laziest workaround. DONT JUDGE ME
                    x = open(os.path.join("pickledFoods"), "wb")
                    pickle.dump(extant_items, x)
                    sys.exit()


def getOldList():
    pickled_file = open(os.path.join("pickledFoods"), "rb")
    return_value = pickle.load(pickled_file)
    print("GOT OLD LIST")
    pickled_file.close()
    return return_value


def runIt():
    index = 0
    while index < 24:
        extant_items = getOldList()
        run_through_dir(extant_items)
        print(extant_items)
        x = open(os.path.join("pickledFoods"), "wb")
        pickle.dump(extant_items, x)
        x.close()
        time.sleep(300)

if __name__ == "__main__":
    runIt()
