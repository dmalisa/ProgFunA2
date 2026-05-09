# Name: Denise Malisa
# Student_ID: s4225650

class Customer:
    def __init__(self, ID, name):
        # initilialize then here
        self.ID = ID
        self.name = name
        
    def display_info(self):
        pass
    
class Member:
    def __init__(self, ID, name, discount_rate):
        self.ID = ID
        self.name = name
        self.discount_rate = discount_rate
        
    def display_info(self):
        pass
        

class PremiumMember:
    def __init__(self, ID, name, discount_rate, service_credit):
        self.ID = ID
        self.name = name
        self.discount_rate = discount_rate
        self.service_credit = service_credit
    
    def display_info(self):
        pass
    

class Service:
    def __init__(self, ID, name, cost_per_hour, require_user_input_hour,
                 service_hour, require_part):
        self.ID = ID
        self.name = name
        self.cost_per_hour = cost_per_hour
        self.require_user_input_hour = require_user_input_hour
        self.service_hour = service_hour
        self.require_part = require_part
        
    def display_info(self):
        pass
    

class Part:
    def __init__(self, ID, name, discount_rate):
        self.ID = ID
        self.name = name
        self.discount_rate = discount_rate
    
    def display_info(self):
        pass

class Records:
    def __init__(self, existing_customers, existing_services, existing_parts):
        self.existing_customers = existing_customers
        self.existing_services = existing_services
        self.existing_parts = existing_parts
    
    def read_customers(self):
        pass
    
    def read_services(self):
        pass
    
    def read_parts(self):
        pass
    
    def list_customers(self):
        pass
    
    def list_services(self):
        pass
    
    def list_parts(self):
        pass

class Main:
    pass