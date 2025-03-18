class Televsion:
    display="LED"
    def __init__(self):
        Televsion.band="Sony"
    def mute(self):
        Televsion.volume=0
        print("Volume",Televsion.volume)
    @classmethod
    def change_mode(cls):
        Televsion.mode="AV"
        print("Telvsion modee",Televsion.mode)
    @classmethod
    def display_details(cls):
        cls.model="Calss 80x "

    @staticmethod
    def netflix():
        Televsion.ur="htts/net"
        print("Conneted ....")

Televsion.netflix()