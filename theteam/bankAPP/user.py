import json

def takeinfor():
    fname = input("Enter your firstname: ")
    lname = input("Enter your lastname: ")
    username = input("Enter username: ")
    passwdn = input("Enter a password: ")

    while True:
        confirmation = input("all informations are valid? yes or no: ")
        if confirmation == "yes":
            break
        elif confirmation == "no":
            takeinfor()
        else:
            continue
        break

    return fname, lname, username, passwdn

class User:
    def __init__(self, accno="None", passwd="None"):
        self.accno = accno
        self.passwd = passwd

    def checkuser(self):
        with open("secrets/secData.txt", "r") as datas:
            for i in datas.readlines():
                data = json.loads(i)
                if self.accno == data["accno"] and self.passwd == data["passwd"]:
                    return True, data["id"]
        return False, "None"

    def creatuser(self):
        fname, lname, username, passwdn = takeinfor()
        print("Creating User:", username, "processing...")
        ids = ""
        accno = ""


        with open("secrets/secData.txt", "r") as datas:
            ids = str(len(datas.readlines())+1)
            accno = str(1000 + int(ids))

        if self.checkuser(accno, passwdn):
            print("The user already exists, pls login...")
            input("Click enter to continue...")
            return "alreadyExist"

        with open("secrets/secData.txt", "a") as userAdd:
            info = f'"id":"{ids}", "accno": "{accno}", "passwd" : "{passwdn}", "balance": "0", "username": "{username}", "fname":"{fname}", "lname":"{lname}"'
            userAdd.write("{" + info + "}\n")

        print("User:", username, "created successfull.")
        input("Click enter to continue...")