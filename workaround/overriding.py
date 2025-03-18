class Smart_Speaker:
    def __init__(self):
        self.volume=15
    def increase_volume(self):
        self.volume=self.volume+4
        print("Sm SP volume",self.volume)

class Smrat_TV(Smart_Speaker):
    def increase_volume(self):
        self.volume=self.volume+1
        print("Sm TV volume",self.volume)
    def connect_to_netflix(self):
        self.web_url="https://netflix.com"
        print(self.web_url)


stv=Smrat_TV()
stv.increase_volume(3)