class Televsion:
    def __init__(self):
        Televsion.brand="Sony"
    def mute(self):
        Televsion.volume=0
        print(Televsion.volume)

    @classmethod
    def change_mode(cls):
        cls.mode="HTMI"
        print(Televsion.mode)
    @classmethod
    def disply_details(cls):
        Televsion.model="xyz"
        print(Televsion.model)
    @staticmethod
    def connect_to_nextfix():
        Televsion.ur="xyz"
        
