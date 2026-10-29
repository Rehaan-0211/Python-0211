from pathlib import Path

def readfilefromfolder():
    path = Path('')
    items = list(path.rglob('*')) #I FUMBLED HERE 1ST
    for i,item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:
        readfilefromfolder()
        name = input("Name the file you want to create:- ")
        p = Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("Input what data you want to add in your file:- ")
                fs.write(data)    # I FUMBLED HERE AS WELL

                print("FILE CREATED SUCCESSFULLY")

        else:
            print("File already exists!")

    except Exception as err:
        print(f"An error occured as{err}")

def readfile():
    try:
        readfilefromfolder()
        name = input("Input which file do you want to read:- ")
        p = Path(name)
        if p.exists():
            with open(p,"r") as fs:
                data = fs.read()       # I FUMBLED HERE TOO
                print(data)

                print("FILE READ SUCCESSFULLY")
        else:
            print("The specified file does not exist")

    except Exception as err:
        print(f"An error occured as{err}")

def updatefile():
    try:
        readfilefromfolder()
        name = input("Input the name of folder which you want to update:- ")
        p = Path(name)
        if p.exists():
            print("Press 1 if you want to change the name of the file") # I FUMBLED HERE
            print("Press 2 if you want to overwrite the current value of your file")
            print("Press 3 if you want to append the values of your file")

            res = int(input("Input your response:- "))

            if res == 1:
                name2 = input("Please enter new value of the file:- ")
                p2 = Path(name2)
                p.rename(p2) # I FUMBLED THIS

            elif res == 2:
                with open(p,"w") as fs:
                    data = input("Enter the new value which you want to input:- ")
                    fs.write(data)

            elif res == 3:
                with open(p,"a") as fs:
                    data = input("Enter the value you want to append:- ")
                    fs.write(" "+ data) # I FUMBLED THIS

            else :
                print("Invalid value has been provided")

        print("UPDATED SUCCESSFULLY")
    except Exception as err:
        print(f"An error occured named as {err}")

def deletefile():
    try:
        readfilefromfolder()
        name = input("Name the file which you want to delete:- ")
        p = Path(name)
        if p.exists():
            p.unlink()    #VERY UNECCASARY FUMBLE GNG

            print("DELETED SUCCESSFULLY")

        else:
            print("No such file exists")

    except Exception as err:
        print(f"An error occured as{err}")

print("Press 1 if you want to create a file")
print("Press 2 if you want to read a file")
print("Press 3 if you want to update a file")
print("Press 4 if you want to delete a file")

check = int(input("Input your command:- "))

if check == 1:
    createfile()
elif check == 2:
    readfile()
elif check == 3:
    updatefile()
elif check == 4:
    deletefile()
else:
    print("Invalid input")

    