# class Smart_Speaker():
#     def __init__(self):
#         self.volume=15
#         super().__init__()
#         print("Default smart speaker ,",self.volume)
# class Smart_TV(Smart_Speaker):
#     def __init__(self):
#         self.volume=20
#
#         print("S,mart TV",self.volume)
# my_smart=Smart_Speaker()

class Parents:
    def show(self):
        
        print("this is parent show")

class Child(Parents):
    def show(self):
        super().show()
        print("this is the child show")

a=Child()
a.show()