class vec2:
    x = 0.0
    y= 0.0

    def __init__(self, x, y):
        print("in init")
        self.x = x
        self.y = y

    def __str__(self):
        msg = str(self.x) + "," + str(self.y)
        print(msg)
        return msg

    def __add__(self, other):
        print("in_add")
        print("self.x =", self.x)
        print("self.y =", self.y)
        print("other.x =", other.x)
        print("other.y =", other.y)
        return vec2(self.x +other.x , self.y + other.y)

if __name__ == "__main__":
    print("vec2 클래스 테스트")
    p=vec2(3,4)
    print("p =" , p)
    
    q = vec2(-1,2)
    print("q = ", q)
    
    r= p+q
    print("r =", r)