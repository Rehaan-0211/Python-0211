from pathlib import Path

def readfilefromfolder():
    path = Path('')
    items = list(path.rglob("*"))
    for i,item in enumerate(items):
        print(f"{i+1} : {item}")

def createfile():
       try: 
        readfilefromfolder()
        name = input("Enter the name of file you wish to create:- ")
        p = Path(name)
        if not p.exists() :
            with open (p,"w") as fs:
                data = input("Input the value you want to enter in your file:- ")
                fs.write(data)

        else:
            print("The file already exists")

       except Exception as err:
           print(f"An error occured as {err}")

def readfile():
    try:    
        readfilefromfolder()
        name = input("Enter the name of the file which you wish to read:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,"r") as fs:
                data = fs.read()
                print(data)

        else:
            print("This file does not exist")

    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:    
        readfilefromfolder()
        name = input("Which folder you want to update:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Press 1 if you wish to change the name of the file")
            print("Press 2 if you wish to overwrite the value of file")
            print("Press 3 if you wish to append the value of file")

            rev = int(input("Input your response:- "))

            if rev == 1:
                name2 = input("Enter the new name of the file:- ")
                p2 = Path(name2)
                p.rename(name2)

            elif rev == 2:
                with open(p,"w") as fs:
                    data = input("Enter your data:- ")
                    fs.write(data)

            elif rev == 3:
                with open(p,"a") as fs:
                    data = input("Input your append value:- ")
                    fs.write(" " + data)

            else:
                print("Invalid response")

        else:
            print("This file does not exist")

    except Exception as err:
        print(f"An error occured as {err}")

def deletefile():
    try:    
        readfilefromfolder()
        name = input("Input the name of the file you wish to delete:- ")
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()

            print("FILE DELETED")

        else:
            print("No such file exists")
    
    except Exception as err:
        print(f"An error occured as {err}")

print("Press 1 if you want to create a file")
print("Press 2 if you want to read a file")
print("Press 3 if you want to update a file")
print("Press 4 if you want to delete a file")

check = int(input("Input your response:- "))

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

    # we did it.