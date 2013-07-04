import os
import time
import shutil
import sys
import logging
def get_folder_size(path):
    totSize = 0
    for root, dirs, files in os.walk(path):
            for name in files:
                totSize += round(os.path.getsize(os.path.join(root, name)) / 1048576)
    return totSize


def get_all_files_in_path(path):
    fileList = []
    for root, dirs, files in os.walk(path):
        for name in files:
            infoList = []
            filePath = os.path.join(root, name)
            infoList.append(filePath)
            stat = os.stat(filePath)
            infoList.append(stat.st_mtime)
            fileList.append(infoList)
    return fileList


def grab_oldest_half_of_files_in_list(fileList):
    fileList = sorted(fileList, key=lambda file: file[1])
    halfPoint = round(len(fileList) / 2)
    fileList = fileList[:halfPoint]
    return fileList


def move_files_to_backup(fileList, backupPath):
    for current_file in fileList:
        try:
            shutil.move(current_file[0].strip(), os.path.join(backupPath))
            logger.info(" ----> Moved : " + current_file[0])
        except (IOError, OSError) as why:
            logger.error(" ---->Failed to copy " + current_file[0] +
                ". Error:" + str(why))

if __name__ == '__main__':
    #logging setup
    logger = logging.getLogger('backupScript')
    logger.setLevel(logging.INFO)
    hdlr = logging.FileHandler(os.path.join(os.path.dirname(os.path.realpath(__file__)), "backupScript.log"))
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr)

    print(sys.argv)
    if len(sys.argv) == 4:
        sourcePath = sys.argv[1]
        destPath = sys.argv[2]
        if  not destPath.endswith('\\'):
            destPath += '\\'
        if not os.path.exists(destPath):
            os.mkdir(destPath)
            logger.info(" ----> Could not find destination folder. Creating " + destPath)
    else:
        print('''The usage of backupScript.py is the following\n
         python backupScript.py sourceDir DestDir folderSizeThresholdinGB\n
         Example: python backupScript.py C:\\files D:\\backup 150''')
        sys.exit()


    mb_size_threshold = sys.argv[3]
    folSizeInMb = get_folder_size(sourcePath)
    if(folSizeInMb > 1000):
        listOfFiles = get_all_files_in_path(sourcePath)
        oldestHalf = grab_oldest_half_of_files_in_list(listOfFiles)
        move_files_to_backup(oldestHalf, destPath)
