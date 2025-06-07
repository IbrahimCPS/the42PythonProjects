import os

def doit():
    if os.name == "nt":
        os.system("""copy .\secrets\secData.txt .\secrets\secData.txt.bak""")
        os.system("""del .\secrets\secData.txt""")
        os.system("""copy .\secrets\secData.txt.process .\secrets\secData.txt""")
    else:
        os.system("cp ./secrets/secData.txt ./secrets/secData.txt.bak")
        os.system("rm ./secrets/secData.txt")
        os.system("cp ./secrets/secData.txt.process ./secrets/secData.txt")