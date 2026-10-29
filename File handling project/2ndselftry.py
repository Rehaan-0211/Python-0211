from pathlib import Path

def readfilefromfolder():
    path = Path('')
    items = list(path.rglob("*"))
    for i,item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
    try:    
        readfilefromfolder()
        name = input("Enter the name of your file you want to create:- ")
        p = Path(name)
        if not p.exists() and p.is_file:
            with open(p,"w") as fs:
                data = input("Enter the data you want to input in your file:- ")
                fs.write(data)

        else:
            print("This file already exists")

            print("THE TASK IS COMPLETED")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:    
        readfilefromfolder()
        name = input("Enter the name of the file that you want to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open (p,"r") as fs:
                data = fs.read() #i fumbled this again
                print(data)
                
        else:
            print("This file does not exist")

        print("READ SUCCESSFULLY")

    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:    
        readfilefromfolder()
        name = input("Enter the name of the file which you wish to update:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 if you want to change the name of the file")
            print("Press 2 if you want to overwrite its value ")
            print("Press 3 if you want to append a value")

            res = int(input("Please enter your response:- "))

            if res == 1:
                name2 = input("Enter the new value of your file:- ")
                p2 = Path(name2)
                p.rename(p2) # I FUMBLED THIS AGAIN

            elif res == 2:
                with open(p,"w") as fs:
                    data = input("Enter the data you want to overwrite:- ")
                    fs.write(data)

            elif res == 3:
                with open(p,"a") as fs:
                    data = input("Enter the data you wanna append:- ")
                    fs.write(" " + data)

            else:
                print("No such file exists")

        print("TASK FINISHED SUCCESSFULLY")
    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:    
        readfilefromfolder()
        name = input("Enter the name of the file you wish to delete:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()

            print("DELETED SUCCESSFULLY")

        else:
            print("No such file exists.")

    except Exception as err:
        print(f"An error occured as {err}")

print("Press 1 if you want to create a file")
print("Press 2 if you want to read a file")
print("Press 3 if you want to update a file")
print("Press 4 if you want to delete a file")

check = int(input("Input your response boss:- "))

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
