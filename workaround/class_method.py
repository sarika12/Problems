class Television:
    display="LED"
    def __init__(self):
        Television.brand="sony"
    def mute(self):
        Television.volume=0
    @classmethod
    def chnage_mode(cls):
        Television.mode="AV"
        print("Television.mode",Television.mode)
    @classmethod
    def display_details(cls):
        cls.model="class x80xk"
        print("TV model",Television.model)
my_tv=Television()
my_tv.display_details()