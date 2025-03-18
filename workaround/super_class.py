class Smart_Speaker:
    def __init__(self):
        self.volume=15
        print("defult smart speaker volume",self.volume)
class Sm_tv(Smart_Speaker):
    def __init__(self):
        self.volum=20
        super().__init__()
        print("smart tv volume",self.volum)


sm_tv=Sm_tv()
