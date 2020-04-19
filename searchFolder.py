import os

for folderName, subfolders, filenames in os.walk("C://Users//EdmarG//Documents//DevNet"):
    print("The current folder is "+ folderName)

    for subfolder in subfolders:
        print(" SUBFOLDER of "+ folderName + ": "+ subfolder)

    for filename in filenames:
        print("File Inside "+ folderName + ":"+ filename)

    print(" ")
    
