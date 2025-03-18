class Television:
    def __init__(self):
        self.vloume=15
        self.channels={1:"Aljezzira",2:"BBC",3:"CNN"}

    def trun_on(self):
        print("tv is trun on")
    def channel_change(self,channel):
         self.channel=channel
         print(f"channel{self.channels[self.channel]}")
    def increase_vloume(self):
        self.vloume=self.vloume+1
        print(self.vloume)
class Smart_Speaker:
    def increase_vloume(self):
        self.vloume=self.vloume+2
        print(self.vloume)


class Smart_TV(Smart_Speaker,Television):
    def connect_to_netfix(self):
        print("connec to netfilx")


obj=Smart_TV()
obj.trun_on()
obj.channel_change(2)
obj.increase_vloume()
obj.connect_to_netfix()