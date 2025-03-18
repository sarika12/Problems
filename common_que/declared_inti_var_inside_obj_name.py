class Televsion:
    def __init__(self, brand,model,screen_size):
        self.brand=brand
        self.model=model
        self.screen_size=screen_size

    def display_derails(self):
        self.resoluation="4K"
        self.display="LED"
        print("TV details")
        print("model",self.brand,self.model)
my_tv=Televsion("sony","class x8-x",65)
my_tv.price=2400
print(my_tv.__dict__)