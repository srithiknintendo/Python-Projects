class Pencil:
    def __init__(self,color,brand):
        self.color = color
        self.brand = brand
        print("Hello")
    def Start(self):
        print("*writing*")
    def Stop(self):
        print("*Stopped writing*")
    def __del__(self):
        print("obj destroyed")

bic = Pencil("Orange","BIC")
del bic
bic.Stop()
