class Vehicle():
    def start(self):
        print("Car has started")


class Car(Vehicle):
    count = 0
    def __init__(self,name,model):
        self.name=name
        self.model=model
        Car.count +=1
        
    def display(self):
        print(self.name,self.model)

    def Count_cars(self):
        print("Cars created:",Car.count)

c1=Car("Bmw","Q3")
c2=Car("Range Rover","2025")
c1.display()
c1.start()
c1.Count_cars()