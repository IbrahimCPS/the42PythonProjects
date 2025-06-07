#IbrahimCPS
def main():
    isCreated = False
    totalContact = 0


    #creat file functions.
    def creat():
        try:
            file = open(r"./contacts.txt", "w")
            file.write("Contacts Lists")
            isCreated = True
        finally:
            file.close()

    #Creat file.
    if isCreated == False:
        creat()

    #Add Contacts 
    def add(name, number):
        added = False
        try:
            file = open(r"./contacts.txt", "a+")
            file.write("\n#no" + ": " + name + " " + number)
            added = True
        except:
            print("Add Fails.")
            raise
        finally:
            file.close()
            if added == True:
                print("Add done...")

    #View contact lists
    def view():
        try:
            file = open(r"./contacts.txt", "r")
            count = 0
            
            #Display Contacts heads
            print("\n\tContacts")
            print("\t" + "=" * 8)

            #Error if file is empty.
            if file.readline() == "":
                raise Exception()
            
            #Display Contacts
            for line in file.readlines():
                line = line.split(" ")
                count += 1
                print(f"#{count}: {line[1]} {line[2]}")
        except:
            print("Add Contact!")
            print("Empty Contacts Listt!!!")
        finally:
            file.close()
            print("Done IbrahimCPS's Contacts...")

    #delete
    def delete(x):
        print(f"I'm so sorry! comming soon. you want to delete No:{x} file")

    while True:
            print("""\n\n   \tMENU""")
            print("#NO   \t" + "=" * 4)
            print("""
 1.\tView.
 2.\tAdd.
 3.\tEdit.
 4.\tDelete.
 5.\tExit.
""")
            print("\nEnter option number to go:", end=" ")
            option = input("")

            #check if input is valid
            if not option.isdigit():
                print("Only Number!!!\n")
                continue

            #Check if input out of range
            if int(option) > 5 or int(option) < 1:
                print("Choose out of range!!!")
                continue
            
            if int(option) == 1:
                view()
                print("Enter any things and press enter: ")
                ask = input("")
                continue
            elif int(option) == 2:
                name = input("Enter name: ")
                while True:
                    number = input("Enter number: ")

                    #check if input is valid
                    if not option.isdigit():
                       print("Only Number!!!\n")
                    break
                add(name, number)
                view()
                continue
            elif int(option) == 3:
                print("Coming soon!\n")
                continue
            elif int(option) == 4:
                while True:
                    view()
                    print("Enter the serial #No. of contact to delete: ", end="")
                    ask = input("")

                    #check if input is valid
                    if not ask.isdigit():
                        print("Only Number!!!\n")
                        continue

                    #check if input is valid range
                    if int(ask) > totalContact or int(ask) < totalContact:
                        print("Choise out of range!!!\n")
                        continue
                    
                    wantToDelete = int(ask)
                    delete(wantToDelete)
                continue
            elif int(option) == 5:
                print("Quitting...")
                exit()
            else:
                print("\nUnkown Answer!")
            break
#main functions
main()
