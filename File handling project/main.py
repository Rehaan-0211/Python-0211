from pathlib import Path
import os
def readfilefromfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, item in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfilefromfolder()
        name = input("please enter your file name:- ")
        p = Path(name)
        if not p.exists():
            with open(p, "w") as fs:
                data = input("What do you want to write in this file:- ")
                fs.write(data)

            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This path already exists")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:    
        readfilefromfolder()
        name = input("Which file do you want to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)

                print("READED SUCCESSFULLY")
        else:
            print("This file does not exist")

    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfilefromfolder()
        name = input("Enter the name of file you want to update :- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of the file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some text in your file")

            res = int(input("Tell your response:- "))

            if res == 1:
                name2= input("Please input your new name:- ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p,'w') as fs:
                    data = input("Enter what you want to enter in your file(THIS WILL OVERWRITE YOUR PREVIOUS DATA!) :-")
                    fs.write(data)

            if res == 3:
                with open(p,'a') as fs:
                            data = input("what do you want to append:-")
                            fs.write(" "+data)

    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:
        readfilefromfolder()
        name = input("Specify the file you wish to delete:- ")
        p = Path(name)

        if p.exists() and p.is_file():
            p.unlink()

            print("FILE REMOVES SUCCESSFULLY")

        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occured named {err}")


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Please specify your input:- "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()