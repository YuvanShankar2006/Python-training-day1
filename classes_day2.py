class vehicle:
    def __init__(self,brand,wheels,fuel_type,milage):  
        self.brand=brand
        self.wheels=wheels
        self.fuel_type=fuel_type
        self.milage=milage
        pass
    def vehicle_details(self):
        print(self.brand)
        print(self.wheels)
        print(self.fuel_type)
        print(self.milage)
class car(vehicle):
    def __init__(self, brand, wheels, fuel_type, milage):
        super().__init__(brand, wheels, fuel_type, milage)    
car1=car("range rover",'4','diesel','12km')
car1.vehicle_details()
car2=car("rolls royce","4","petrol","10 km")
car2.vehicle_details()
class bike(vehicle):
    def __init__(self,brand,wheels,fuel_type,milage):       
         
        super().__init__(brand,wheels,fuel_type,milage)
bike1=bike("BMW","2","petrol","26")
bike2=bike("splendor","2","diesel","100")
bike3=bike("ducati","2","petrol","23")
bike1.vehicle_details()
bike2.vehicle_details()
bike3.vehicle_details()
