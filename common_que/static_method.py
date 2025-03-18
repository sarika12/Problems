class Televsion:
    disply="LED"
    def __init__(self):
        Televsion.brand="sony"

    def mute(self):
        Televsion.vloume=0
        print("volume",Televsion.vloume)
    @classmethod
    def change_mode(cls):
        Televsion.mode="AV"
        print("mode",Televsion.mode)
    @classmethod
    def display_details(cls):
        cls.model="XYZ--XYZ"
        print("TV model",Televsion.model)

    @staticmethod
    def connect_to_netfix():
        Televsion.web_url="htts//Netfix"
        print("Connect to netfix")
Televsion.connect_to_netfix()
# print(Televsion.__dict__)
my_tv=Televsion()
my_tv.mute()
my_tv.change_mode()
my_tv.connect_to_netfix()