class Vec2:
    x = 0.0
    y = 0.0

    def __init__(self, x, y):
        self.x =x
        self.y =y
        print("i-2) self.x =", self.x)
        print("i-3) self.y =", self.y)

    def __str__(self):
        msg = "(" + str(self.x) +"," + str(self.y) +")"
        print("msg =", msg)
        return msg

    def __add__(self, other):
        print("a-1) in add")
        print("a-2) self.x =",self.x )
        print("a-3)self.y = ", self.y)
        print("a-4)other.x = ", other.x)
        print("a-5) other.y", other.y)
        return Vec2(self.x + other.x , self.y +other.y)
    

#vec2 클래스 테스트
if __name__ == "__main__":

    print("m-1) vec2 클래스 테스트")
    p=Vec2(3,4)
    print("p=", p)

    q=Vec2(-1, 2)
    print("m-3) q=", q)

    r=p+q
    print("m-4) r=", r)