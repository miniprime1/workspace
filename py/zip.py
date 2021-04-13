import os, sys
from zipfile import *

print("Zip, version 1.0")
print("Copyright (c) 2020 miniprime1\n")

print("Options")
print("1. Create (Create zip file from directory)")
print("2. Extract (Extract zip file to directory)")
print("3. Read (Read zip file, and show detail of files)")
print("4. Exit")
option = input("Your choice: ")

if option == "1":
    path = input("\nEnter the path of the zip file to save: ")
    src = input("Enter path of the source directory: ")
    zip = ZipFile(path, 'w')
    for folder, subfolders, files in os.walk(src):
        for file in files:
            zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), src), compress_type = ZIP_DEFLATED)

    print("\nDone!")
    
    zip.close()

elif option == "2":
    path = input("\nEnter the path of the zip file to open: ")
    out = input("Enter the path of the output directory: ")
    zip = ZipFile(path)
    zip.extractall(out)
    print("\nDone!")
    zip.close()

elif option == "3":
    i = 0
    path = input("\nEnter the path of the zip file to open: ")
    zip = ZipFile(path)
    for file in zip.namelist():
        i = i + 1
        info = zip.getinfo(file)
        print("\n" + str(i) + ". " + str(info.filename))
        print("Name: " + str(info.filename))
        print("Date Time: " + str(info.date_time))
        print("Compressed Size: " + str(info.compress_size))
        print("File Size: " + str(info.file_size))

elif option == "4":
    sys.exit()

else:
    print("\nError: invalid choice")

input("\nPress enter key to exit") 
