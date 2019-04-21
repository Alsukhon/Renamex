import os
import shutil

#Define current and new file directories
directory = os.getcwd()
dstn = directory+"//RenamEx//"

#Ask for current and target extensions
inputExt = input("Input extension: ")
outputExt = input("Output extension: ")

#Create the new directory
os.mkdir(dstn)

#For all files with current extension, copy them to new directory
for file in os.listdir(directory):
    if file.endswith(inputExt):
        shutil.copy(str(directory+"//"+file),dstn)

#Go to that directory and rename all file extensions
        os.chdir(dstn)
        newName = str(file.split(inputExt)[0]) + str(outputExt)
        os.rename(file, newName)

#Cleanup
del directory
del dstn
del inputExt
del outputExt
del newName
