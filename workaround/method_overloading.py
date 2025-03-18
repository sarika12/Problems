class Televsion:
    def __init__(self):
        self.channels={1:"ajjezzira",2:"BBC",3:"CNN",4:"FIFA TV"}
        self.channel=3
    def change_channel(self,channel):
        # self.channel
        print(f"chnagging TV channel to {self.channels[channel]}")
    def change_channel(self,command):
        self.command=command
        if self.command=="up":
            self.channel+=1
            print(f"chnaging smart TV channel to {self.channels[self.channel]}")
        elif self.command == "down":
            self.channel -= 1
            print(f"chnaging smart TV channel to {self.channels[self.channel]}")

        else:
            print("have you press wrong buttom")
