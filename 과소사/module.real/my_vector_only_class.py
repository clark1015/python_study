class Vec_3:

    x=0.0
    y=0.0

    def __init__(self, x, y):
        print("\nin init")
        self.x = x
        self.y = y
        print("in init, self.x=",self.x)
        print("in init, self.y=", self.y)

    def __Str__(self):
        msg = "(" + str(self.x) + "," + str(self.y) + ")"
        print("\nin str.msg =", msg)
        return msg

    def __add__(self, other):
        print("\nin add")
        print("self.x =", self.x)
        print("self.y =", self.y)
        print("other.x = ", other.x)
        print("other.y = ", other.y)
        return Vec_3(self.x + other.x , self.y +other.y)