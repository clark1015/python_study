class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def area(self):
        print("도형 면적 계산")

    def perimeter(self):
        print("도형 둘레 계산")

class Rectangle(Shape):
    def __init__(self, x, y, w, h):
        super().__init__(x, y)
        self.w = w
        self.h = h

    def area(self):
        print("상위 클래스 오버라이딩")
        return self.w *self.h
    
    def perimeter(self):
        print("상위 클래스 오버라이딩")
        return 2*(self.w + self.h)
