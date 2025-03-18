class Televsion:
    def __init__(self):
        self.channel={1:"Aljezzira",2:"BBC",3:"CNN"}
    def trun_on(self):
        print("this is TV on.")
    def change_channel(self,channel):
        print(f"chnaging chnanne to{self.channel[channel]} ")
class Flat_Tv(Televsion):
    def HDMI_mode(self):
        self.mode="HDMI"
        print(f"mode{self.mode}")
my_fl=Flat_Tv()
my_fl.HDMI_mode()
my_fl.change_channel(1)