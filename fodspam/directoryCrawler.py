import os
import pickle
import time
import sys
import datetime
import re
import logger


root_path = "\\\\10.19.110.117\Group\Public Access\Camp\Today's Menu"
file_path = os.path.join("pickledFoods")
extant_items = []
recently_emailed = False
now = datetime.datetime.now()
todays_date = str(now.day)


def run_through_dir(extant_items, path=root_path):
    for file_or_folder in os.listdir(path):
        pathName = os.path.join(path, file_or_folder)
        if os.path.isdir(pathName):
            run_through_dir(extant_items, pathName)
        else:
            if file_or_folder in extant_items:
                pass
            elif file_or_folder not in extant_items:
                log.info("FOUND A NEW FILE!! New item: " + pathName)
                extant_items.append(file_or_folder)
                # quick regex to strip the date out of the filename
                date_in_file_name = re.search('(\d+)', file_or_folder).group(0)
                log.info("Date found in title is: " + date_in_file_name)
                if "~" in file_or_folder:
                    log.info("oops just a temporary file, never mind!")
                elif "~" not in file_or_folder and ".docx" in file_or_folder and todays_date == date_in_file_name:
                    os.system("ruby " + "spammer.rb " + "\"" + pathName + "\"")  # worlds ugliest and laziest workaround. DONT JUDGE ME
                    log.info("Emailed!")
                    x = open(os.path.join("pickledFoods"), "wb")
                    pickle.dump(extant_items, x)
                    return file_or_folder


def getOldList():
    pickled_file = open(os.path.join("pickledFoods"), "rb")
    return_value = pickle.load(pickled_file)
    log.info("GOT OLD LIST")
    pickled_file.close()
    return return_value


def runIt():
    pollCount = 0
    while True:
        print("polling folder: " + root_path + " ........")
        extant_items = getOldList()
        file = run_through_dir(extant_items)
        if file:
            log.info("Found file after " + str(pollCount) + " polling intervals. Quitting. ")
            print("DONE")
            sys.exit(0)
        x = open(os.path.join("pickledFoods"), "wb")
        pickle.dump(extant_items, x)
        x.close()
        pollCount +=1
        time.sleep(600)

if __name__ == "__main__":
    log = logger.Logger().get_logger()
    runIt()
