#lex_auth_012736349701922816604
#Start writing your code here
#lex_auth_012736349701922816604
#Start writing your code here
class vehicle:
    def __init__(self):
        self.__vehicle_id = None
        self.__vehicle_type = None
        self.__vehicle_cost = None
        self.__vehicle_amount = None
        self.__premium_amount = None
        
    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id
        
    def get_vehicle_id(self):
        return self.__vehicle_id
        
    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type
        
    def get_vehicle_type(self):
        return self.__vehicle_type
        
    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost
        
    def get_vehicle_cost(self):
        return self.__vehicle_cost
        
    def set_vehicle_amount(self, vehicle_amount):
        self.__vehicle_amount = vehicle_amount
        
    def get_vehicle_amount(self):
        return self.__vehicle_amount
        
    def get_premium_amount(self):
        return self.__premium_amount
        
    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = 0.02 * self.__vehicle_cost
            
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = 0.06 * self.__vehicle_cost 
            
        else:
            print("Invalid vehicle type")
            self.__premium_amount = None
        
    def display_vehicle_details(self):
        if self.__premium_amount is not None:
            print("vehicle ID : ", self.__vehicle_id)
            print("vehicle Type : ", self.__vehicle_type)
            print("vehicle Cost : ", self.__vehicle_cost)
            print("Premium Amount: ", self.__premium_amount)
            

v1 = vehicle()
v1.set_vehicle_id(101)
v1.set_vehicle_type("Two Wheeler")
v1.set_vehicle_cost(50000)

v1.calculate_premium()
v1.display_vehicle_details()

v2 = vehicle()
v2.set_vehicle_id(102)
v2.set_vehicle_type("Four Wheeler")
v2.set_vehicle_cost(200000)

v2.calculate_premium()
v2.display_vehicle_details()
    
