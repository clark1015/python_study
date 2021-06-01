class Vehicle:
    def __init__(self, make, model, color, price):
        self.make = make #메이커
        self.model = model#모델
        self.color = color #자동차의 색상
        self.price = price#자동차 가격

    def getMake(self):
        return self.make

    def setMake(self, make):
        self.make = make

    def getDesc(self): #차량에 대한 정보를 문자열로 나열
        return "차량 = "+ str(self.make) + ", " + str(self.model) + ", " + str(self.color) + ", " + str(self.price) 
        print("ggg")


class Truck(Vehicle):
    def __init__(self, make, model, color, price, payload):
        super().__init__(make, model, color, price)
        self.payload = payload

    def setPayload(self, payload):
        self.payload = payload       #setter

    def getPayload(self):            #getter
        return self.payload

def main():
    myTruck = Truck("Null", "Model S", "White", 10000, 2000)
    myTruck.setMake("Tesla")
    myTruck.setPayload(2000)
    print(myTruck.getDesc())

main()