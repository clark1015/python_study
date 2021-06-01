class Car:
    def __init__(self, speed):
        self.speed = speed

    def setSpeed(self, speed):
        self.speed = speed

    def getsDesc(self):
        return "차량 = " + str(self.speed)
