import os
import json
import commit

def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Bank:
    def __init__(self, acc, passwd):
        clean()
        self.__accno = acc
        self.__passwd = passwd

        self.__ids, self.__fname, self.__lname, self.__username = "","","",""

        with open("secrets/secData.txt", "r") as datas:
            for i in datas.readlines():
                data = json.loads(i)
                if self.__accno == data["accno"] and self.__passwd == data["passwd"]:
                    self.__ids = data["id"]
                    self.__fname = data["fname"]
                    self.__lname = data["lname"]
                    self.__username = data["username"]
                    self.__balance = data["balance"]

    def __checkBalance(self):
        clean()
        print("Your Account balance:", self.__balance + "$")

    def __showMyInfor(self):
        clean()
        print(f"""
             First Name:      {self.__fname}
             Last Name:       {self.__lname}
             Username:        {self.__username}
             Password:        {self.__passwd}
             Account Number:  {self.__accno}
        """)

    def __deposit(self):
        clean()
        while True:
            amount = input("Enter the deposit amount: ")
            try:
                int(amount)
            except:
                print("Please enter a valid amount!")
                input("Click enter to continue...")
                continue

            self.__balance = str(int(self.__balance) + int(amount))

            with open("secrets/secData.txt.process", "w") as transfers:
                with open("secrets/secData.txt", "r") as users:
                    for i in users.readlines():
                        user = json.loads(i)
                        if self.__accno == user["accno"]:
                           info = f'"id":"{user["id"]}", "accno": "{user["accno"]}", "passwd" : "{user["passwd"]}", "balance": "{self.__balance}", "username": "{user["username"]}", "fname":"{user["fname"]}", "lname":"{user["lname"]}"'
                           transfers.write("{" + info + "}\n")
                        else:
                           info = f'"id":"{user["id"]}", "accno": "{user["accno"]}", "passwd" : "{user["passwd"]}", "balance": "{user["balance"]}", "username": "{user["username"]}", "fname":"{user["fname"]}", "lname":"{user["lname"]}"'
                           transfers.write("{" + info + "}\n")

            commit.doit()

            with open("secrets/history.txt", "a") as hists:
                hist = f'"accno":"{self.__accno}", "type":"deposit", "amount":"{amount}", "time":"12PM"'
                hists.write("{" + hist + "}\n")

            print(f"Deposit: {int(amount)} success...")
            self.__checkBalance()
            break

    def __transfer(self):
        clean()
        while True:
            accountTo = input("Enter account number: ")
            amount = input("Enter the transfer amount: ")
            try:
                int(amount)
                int(accountTo)
            except:
                print("Please enter a valid information!")
                input("Click enter to continue...")
                continue

            isthebankvalid = False
            with open("secrets/secData.txt", "r") as users:
                for i in users.readlines():
                    user = json.loads(i)
                    if accountTo == user["accno"]:
                        isthebankvalid = True
                        break
                    else:
                        continue

            if not isthebankvalid:
                print("The bank account is invalid or transfer to this bank is not supported")
                while True:
                    confirmation = input("Do you want retry again? yes or no: ")
                    if confirmation == "yes":
                        self.__transfer()
                    elif confirmation == "no":
                        break
                    else:
                        continue
                return

            if int(amount) > int(self.__balance) or int(amount) == 0:
                print("Check the amount and check your balance")
                break

            if self.__accno == accountTo:
                print("You can't transfer to your self!")
                break

            self.__balance = str(int(self.__balance) - int(amount))

            with open("secrets/secData.txt.process", "w") as transfers:
                with open("secrets/secData.txt", "r") as users:
                    for i in users.readlines():
                        user = json.loads(i)
                        if accountTo == user["accno"]:
                           info = f'"id":"{user["id"]}", "accno": "{user["accno"]}", "passwd" : "{user["passwd"]}", "balance": "{self.__balance}", "username": "{user["username"]}", "fname":"{user["fname"]}", "lname":"{user["lname"]}"'
                           transfers.write("{" + info + "}\n")
                        else:
                            info = f'"id":"{user["id"]}", "accno": "{user["accno"]}", "passwd" : "{user["passwd"]}", "balance": "{user["balance"]}", "username": "{user["username"]}", "fname":"{user["fname"]}", "lname":"{user["lname"]}"'
                            transfers.write("{" + info + "}\n")

            commit.doit()

            with open("secrets/history.txt", "a") as hists:
                hist = f'"accno":"{self.__accno}", "type":"transfer", "amount":"{amount}", "toaccno":"{accountTo}", "time":"12PM"'
                hists.write("{" + hist + "}\n")

            self.__checkBalance()
            print(f"Transfer of: {int(amount)} success...\nTo Acoount number: {accountTo}")
            break

    def __closeAcc(self):
        clean()
        self.__checkBalance()
        self.__showMyInfor()


        print("If you have money it will be send to government's account!")
        while True:
            confirmDel = input("Confirm to delete your account! yes or no: ")
            if confirmDel == "yes":
                break
            elif confirmDel == "no":
                return False
            else:
                continue

        with open("secrets/secData.txt.process", "w") as closeAcc:
            with open("secrets/secData.txt", "r") as users:
                for i in users.readlines():
                    user = json.loads(i)
                    if self.__accno == user["accno"] and self.__passwd == user["passwd"]:
                        continue
                    info = f'"id":"{user["id"]}", "accno": "{user["accno"]}", "passwd" : "{user["passwd"]}", "balance": "{user["balance"]}", "username": "{user["username"]}", "fname":"{user["fname"]}", "lname":"{user["lname"]}"'
                    closeAcc.write("{" + info + "}\n")


        commit.doit()
        print("Account successfully closed...")
        return True

    def __history(self):
        clean()
        print("History...")
        with open("secrets/history.txt", "r") as hists:
            for i in hists.readlines():
                hist = json.loads(i)
                if self.__accno == hist["accno"]:
                    if hist["type"] == "transfer":
                        print(f'Debit: {hist["amount"]} Transfer To: {hist["toaccno"]} Time: {hist["time"]}')
                    else:
                        print(f'Deposit: {hist["amount"]} Time: {hist["time"]}')
                else:
                    if hist["type"] == "transfer" and hist["toaccno"] == self.__accno:
                        print(f'Credit: {hist["amount"]} From: {hist["accno"]} Time: {hist["time"]}')
        print("Done.")

    def menu(self):
        while True:
            clean()
            print("+" + "=" * 27 + "+")
            print("+welcome To The theTeam Bank+")
            print("+" + "=" * 27 + "+")
            print("Welcome mr/mrs,", self.__username + "!")
            print(f"+ Account balance: {self.__balance}$")

            print("""
            MENU:
               1. Check Balance.
               2. Deposit.
               3. Transfer.
               4. History.
               5. Show my account details.
               6. EXIT.
               0. Close Account.
               """)
            choice = input("Enter your choice: ")

            try:
                int(choice)
            except:
                print("Please enter a valid choice!")
                input("Click enter to continue...")
                continue

            choice = int(choice)

            if choice < 0 or choice > 6:
                print("Please enter a range choice!")
                input("Click enter to continue...")
                continue

            if choice == 1:
                self.__checkBalance()
                input("Click enter to continue...")
                continue
            elif choice == 2:
                self.__deposit()
                input("Click enter to continue...")
                continue
            elif choice == 3:
                self.__transfer()
                input("Click enter to continue...")
                continue
            elif choice == 4:
                self.__history()
                input("Click enter to continue...")
                continue
            elif choice == 5:
                self.__showMyInfor()
                input("Click enter to continue...")
                continue
            elif choice == 6:
                break
            elif choice == 0:
                if self.__closeAcc():
                    input("Click enter to continue... exit")
                    break
                else:
                    input("Click enter to continue...")
                    continue
            else:
                print("Please respect the bank policy.")
                input("Click enter to continue...")
                continue
