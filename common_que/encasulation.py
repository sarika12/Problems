class Televsion:
    def __init__(self):
        self.chanel="BBC"
        self._volume=15
        self.__brand="sony"

    def tru_on(self):
        print(f"the{self.__brand} televsion no trun on")
    def _change_channel(self):
        print(f"chnnel has change{self.chanel}")
    def __adjust_vloume(self):
        print(f"the volume has been adjuexted to {self._volume}")

my_tv=Televsion()
print(my_tv)
my_tv.__adjust_vloume(30)