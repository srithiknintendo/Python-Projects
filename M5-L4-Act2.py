class Base:
    def __init__(self):
        self.a = "Geeksforgeeks"
        self._c= "Geeksforgeeks"
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling Private number from base class")
        print(self._c)
obj1 = Base()
print(obj1.a)