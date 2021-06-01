class Vehicle:
    def __init__(self, in_speed= 0, in_direction="straight"):
        print("start point")
        self.__speed = in_speed
        self.__direction = in_direction
        print("self.__speed =", self.__speed)
        print("self.__direction =", self.__direction)

    def setSpeed(self, in_speed=0):
        print("스피드 세팅")
        self.__speed =in_speed
        print("self.__speed=",self.__speed)

    def getSpeed(self):
        print("현재 속도 출력")
        print("self.__speed =",self.__speed)

    def turn(self, in_direction):
        print("")
        self.__direction = in_direction
        print("self__direction=", self.__direction)

    def getDirection(self):
        print("현재 방향")
        print("self.__direction =", self.__direction)

    def getDescription(self):
        msg = "vehicle: (" +str(self.__speed) +", "+ str(self.__direction)
        print("msg=", msg)

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass

class Bus(Vehicle):
    pass

class Main():
    def car_instnace(self):
        print("mycar instance")
        myCar =Car()
        print("myCar:", myCar)

        myCar.getSpeed()
        myCar.setSpeed(100)
        myCar.getSpeed()

        myCar.getDirection()
        myCar.turn("right")
        myCar.getDirection()

        myCar.getDescription()

m=Main()
m.car_instnace()