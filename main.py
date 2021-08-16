class Car(object):
    def __init__(self,model,color,company,speedLimit):
        self.model = model
        self.color = color
        self.company = company
        self.speedLimit = speedLimit
    
    def start(self):
        print("car started")

    def stop(self):
        print("car stoped") 

    def accelerate(self):
        print("accelerating")

audi = Car("a6","red","audi","120")
print(audi.start())
print(audi.stop())
print(audi.accelerate())

print(audi.color)