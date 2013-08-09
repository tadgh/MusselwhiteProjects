import os
import time
import shutil
import sys
import logger

def get_folder_size(path):
    totSize = 0
    for root, subdirectories, files in os.walk(path):
            for name in files:
                totSize += round(os.path.getsize(os.path.join(root, name)) / 1048576)
    return totSize

def get_top_level_files_in_path(path):
    file_list = []
    for file_or_folder in os.listdir(path):
        file_path = os.path.join(path, file_or_folder)
        mod_time = (os.stat(file_path)).st_mtime
        file_list.append([file_path, mod_time])

    print("starting list dump")
    for item in file_list:
        print(item)
    print("ending list dump")

    return file_list


def grab_oldest_half_of_files_in_list(fileList):
    fileList = sorted(fileList, key=lambda file: file[1])
    halfPoint = round(len(fileList) / 2)
    fileList = fileList[:halfPoint]
    return fileList


def move_files_and_folders(file_or_folder_list, destination_path):
    for file_or_folder in file_or_folder_list:
        try:
            shutil.move(file_or_folder[0], destination_path)
            logger.info(" ----> " + file_or_folder[0] + "\t" "---->" + "\t" + destination_path)
        except(IOError, OSError, shutil.Error) as error:
            logger.error(" ----> Failed to copy " + file_or_folder[0] +
                ". Error:" + str(error))


def parse_arguments():
    print(sys.argv)
    if len(sys.argv) == 4:
        sourcePath = sys.argv[1]
        destPath = sys.argv[2]
        threshold_in_mb = int(sys.argv[3])

        #if not destPath.endswith('\\'):
         #   destPath += '\\'
        if not os.path.exists(destPath):
            os.mkdir(destPath)
            logger.info(" ----> Could not find destination folder. Creating " + destPath)
    else:
        print('''The usage of backupScript.py is the following\n
         python backupScript.py sourceDir DestDir FolderSizeThreshold\n
         Example: python backupScript.py C:\\files D:\\backup 1000''')
        sys.exit()
    return sourcePath, destPath, threshold_in_mb

def initiate_half_backup(sourecPath, destPath):
        listOfFiles = get_top_level_files_in_path(sourcePath)
        oldestHalf = grab_oldest_half_of_files_in_list(listOfFiles)
        move_files_and_folders(oldestHalf, destPath)

if __name__ == '__main__':
    logger = logger.Logger().getLogger("test")
    sourcePath, destPath, threshold_in_mb = parse_arguments()
    if(get_folder_size(sourcePath) > threshold_in_mb):
        initiate_half_backup(sourcePath, destPath)
