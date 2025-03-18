class Televsion:
    def __init__(self):
        self.channel="BBC"
        self._volume=15
        self.__brand="sony"
    def trun_on(self):
        print(f"the {self.__brand} tv is now on ")
    def _change_channel(self,channel):
        print(f"the channel has been changed to {channel}")
    def __adjuest_volume(self,volume):
        print(f"The volume has been adjuest to {volume}")


obj=Televsion()
obj.trun_on()
obj._change_channel("XYZ")
# obj.__adjuest_volume()
print(obj._volume)
print(obj.__brand)
obj.__adjuest_volume(13)

