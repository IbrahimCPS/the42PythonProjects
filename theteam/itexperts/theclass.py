"""lists = {
    "names": {
        0: "AnonymouZ",
        1: "Abdurrazak",
        2: "Khan",
        3: "Nabahani",
        4: "IbrahimCPS"
    },
    "stuffs": {
        0: ["powerbank", "cap"],
        1: ["Computer", "Usb-drive"],
        2: ["Computer-Charger"],
        3: ["Laptop", "waya"],
        4: ["banada_komie"]
    }
}
"""
class TheTeam:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def callme(self):
        print("Hi,", self.name)