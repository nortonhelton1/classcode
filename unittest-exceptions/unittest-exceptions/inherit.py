
class Car: 
    def __init__(self, make, model): 
        self.make = make 
        self.model = model 
    
    def drive(self): 
        print("DRIVE")
    
    def fill_up(self): 
        print("FILL UP GAS")

car = Car("Honda", "Accord")
#car.drive() 
#car.fill_up() 

class ElectricCar(Car): # ElectricCar inherits from Car. ElectricCar is a subclass, Car is parent/super class 
    def __init__(self, make, model): 
        # always make sure to call the init of the super class 
        super().__init__(make, model)
    
    # overriding the fill_up function 
    def fill_up(self): 
        print("CHARGE THE CAR")
        

class ElectricScooter(ElectricCar): 
    def __init__(self, make, model): 
        super().__init__(make, model)
    
    def fill_up(self): 
        print("CHARGE ELECTRIC SCOOTER")


electric_car = ElectricCar("Tesla", "Model X") 
electric_car.drive() 
electric_car.fill_up() 

electric_scooter = ElectricScooter("MAKE", "MODEL")
electric_scooter.fill_up() 

# Python does allow multiple inheritance 