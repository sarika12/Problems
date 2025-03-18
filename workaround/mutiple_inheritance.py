class Televsion:
    def __init__(self):
        self.volume=15
        self.channels={1:"Aljeezzira",2:"BBC",3:"CNN"}
    def trun_on(self):
        print("the tv is on.")
    def change_channel(self,channel):
        # self.channel=channel
        print(f"channel type {self.channels[channel]}")
    def increase_volume(self):
        self.volume=self.volume+2
        print("TV",self.volume)

class Smart_Speaker:
    def increase_volume(self):
        self.volume=self.volume+1
        print("Sm SP volume",self.volume)

class Smrat_TV(Smart_Speaker,Televsion):
    def connect_to_netflix(self):
        self.web_url="https://netflix.com"
        print(self.web_url)

my_smart_tv=Smrat_TV()
my_smart_tv.trun_on()
my_smart_tv.change_channel(2)
my_smart_tv.increase_volume()
my_smart_tv.connect_to_netflix()