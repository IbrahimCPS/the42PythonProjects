class ValidateMe:
    getme = "iget"
    def __init__(self, name):
        self.name = name
        self.nameList = ["IbrahimCPS", "Abdurrazak", "Nabahani", "AnonymouZ", "Khan"]

    def saymyname(self):
        print("Hello,", self.name)

    def doyouknowme(self):
        for i in self.nameList:
            if i == self.name:
                print("yes sir, Your're welcome!")
                return
        print("no, sir! we dont have your name in the lists")
        return