import bankLogin
import user
from bankLogin import clean


def confirmtocreateuser():
    while True:
        confirmation = input("Do you want to create the user? yes or no: ")
        if confirmation == "yes":
            return True
        elif confirmation == "no":
            return False
        else:
            continue

while True:
    clean()
    print("+" + "=" * 27 + "+")
    print("+welcome To The theTeam bank+")
    print("+" + "=" * 27 + "+")
    print("You're welcome.")

    accountNumber = input("Enter your account number: ")
    password = input("Enter your password: ")

    log = user.User(accountNumber, password)
    isUser, userID = log.checkuser()

    if not isUser:
        #print("no! the user does not exist.")
        if confirmtocreateuser():
            if log.creatuser() == "alreadyExist":
                continue
        else:
            continue

    accountLogin = bankLogin.Bank(accountNumber, password)
    accountLogin.menu()

    print("Logout success...\n+" + "=" * 25 + "+\n+THANK YOU FOR CHOOSING US+\n+" + "=" * 25 + "+")
    break
