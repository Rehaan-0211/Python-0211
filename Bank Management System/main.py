import json
import random
import string
from pathlib import Path

class Bank:

    data = []
    database = 'data.json'

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")

    except Exception as err:
        print(f"An exception occured as{err}")

    @classmethod
    def __update(cls):
        with open(cls.database,"w") as fs:
            fs.write(json.dumps(cls.data))

    @classmethod
    def __randomgenerate(cls):
        alpha = random.choices(string.ascii_letters,k = 3)
        num = random.choices(string.digits,k = 3)
        spchar = random.choices("!@#$%&*",k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)

    def createaccount(self):
        info = {
            "name" : input("Name please:- "),
            "age" : int(input("Enter your age:- ")),
            "email" : input("Your email:- "),
            "pin" : int(input("Your pin:- ")),
            "accountNo." : Bank.__randomgenerate(),
            "balance" : 0
        }

        if info['age'] < 18 or len(str(info['pin'])) !=4 or info['name'] == "Shivam":
            print("Review your credentials and try again")
        else:
            print("Account has been created successfully------------------------------------")
            for i in info:
                print(f"{i} : {info[i]}")

            print("Note down your account number for further use.")

            Bank.data.append(info)

            Bank.__update()

    def depositmoney(self):
        accnumber = input("Please enter your acc number:- ")
        pin = int(input("Your pin:- "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No data found")

        else:
            amount = int(input("Enter the amount you wanna deposit:- "))
            if amount <= 0:
                print("Invalid deposit")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount debited successfully")

    def withdrawmoney(self):
            accnumber = input("Please enter your acc number:- ")
            pin = int(input("Your pin:- "))
    
            userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
    
            if userdata == False:
                print("No data found")
    
            else:
                amount = int(input("Enter the amount you wanna withdraw:- "))
                if userdata[0]['balance'] < amount:
                    print("You don't have that much money in your account.")
    
                else:
                    userdata[0]['balance'] -= amount
                    Bank.__update()
                    print("Amount withdrawn successfully")


    def showdetails(self):
        accnumber = input("Please enter your acc number:- ")
        pin = int(input("Your pin:- "))
            
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
        print("Your info is as follows:- \n\n")
        for i in userdata[0]:
            print(f"{i} : {userdata[0][i]}")


    def updatedetails(self):
        accnumber = input("Please enter your acc number:- ")
        pin = int(input("Your pin:- "))
                   
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin] 

        if userdata == False:
            print("No such user exists")

        else:
            print("CAUTION:- Do not try to change your age,account number and balance.")
            print("Fill details if you wish to change some detail:- ")

            newdata = {
                "name" : input("Enter the new name value if you wish to change it."),
                "email" : input("Enter the new email if you wish to change it") ,
                "pin" : input("Enter new pin if you wish to change your pin")
            }

            if newdata["name"] == "":
                newdata["name"] = userdata[0]['name']
            if newdata["email"] == "":
                newdata["email"] = userdata[0]['email']
            if newdata["pin"] == "":
                newdata["pin"] = userdata[0]['pin']

            newdata["age"] = userdata[0]['age']
            newdata["accountNo."] = userdata[0]['accountNo.']
            newdata["balance"] = userdata[0]['balance']

            if type(newdata['pin']) == str:
                newdata['pin'] = int(newdata['pin'])

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Update initiated.")
                

    def delete(self):
        accnumber = input("Please enter your acc number:- ")
        pin = int(input("Your pin:- "))
                           
        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("No such data exists")

        else:
            print("Print n if you want to rethink this choice else type anything")
            if check == 'n' or check == "N":
                print("Delete initialization terminated successfully")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account deleted successfully")
                Bank.__update()

user = Bank()


print("Press 1 to create an account")
print("Press 2 to deposit money in your account")
print("Press 3 to withdraw your money")
print("Press 4 to check details")
print("Press 5 to update details")
print("Press 6 to delete your account")

check = int(input("Enter your response:- "))
if check == 1:
    user.createaccount()

elif check == 2:
    user.depositmoney()

elif check == 3:
    user.withdrawmoney()

elif check == 4:
    user.showdetails()

elif check == 5:
    user.updatedetails()

elif check == 6:
    user.delete()