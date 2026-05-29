# Name: Denise Malisa
# Student_ID: s4225650

import os
import sys

class Customer:
    """_summary_ This class defines the structure of a basic customer object
    with a ID and a name
    """
    # method is the constructor of the class customer
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        
    # method to get customerID   
    def get_ID(self):
        return self.ID
    
    # method to get name   
    def get_name(self):
        return self.name
        
    def display_info(self):
        print("ID: " + self.ID + ", name: " + self.name)
        
class Member:
    """_summary_ This class defines the structure of a member object 
    with the respective properties for a member
    """
    discount_rate = 0.10
    
    # constructor of the member class
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        
    # method to get memberID   
    def get_ID(self):
        return self.ID
    
    # method to get name   
    def get_name(self):
        return self.name
    
    # method to get discount rate   
    def get_discount_rate(self):
        return self.discount_rate
    
    # method to set a new discount rate
    def set_discount_rate(self, new_discount):
        self.discount_rate = new_discount
        
    # method returns the discount cost    
    def get_discount(self, service_cost):
        return self.discount_rate * service_cost
            
    def display_info(self):
        print(f'ID: {self.ID}, name: {self.name}, discount rate: {self.discount_rate}')
        
class PremiumMember (Member):
    """_summary_ This class defines the structure of a premium member object 
    with the respective premium member attributes and inherits from the Member class
    """
    # constructor for the premium member class
    def __init__(self, ID, name, service_credit, discount_rate = 0.10):
        super().__init__(ID, name)
        self.discount_rate = discount_rate
        self.service_credit = service_credit
    
    # method returns the credit   
    def get_credit(self, total_cost):
        new_service_credit = int(total_cost/100)
        return new_service_credit
    
    # method updates the users credit   
    def update_credit(self, new_credit):
        self.service_credit += new_credit
    
    def display_info(self):
        print(f"ID: {self.ID}, name: {self.name}, discount rate: {self.discount_rate}, service credit: {self.service_credit}")

class Service:
    """_summary_ This class defines the structure a service object with the respective 
    attributes required to represent a service
    """
    # constructor for the service class
    def __init__(self, ID, name, cost_per_hour, require_user_input_hour,
                 service_hour, require_part):
        """
        Args:
            ID (_type_): _description_ The ID for the respective service
            name (_type_): _description_ The name of the service
            cost_per_hour (_type_): _description_ The cost of the service
            require_user_input_hour (_type_): _description_  The hours the users specifies for the service
            service_hour (_type_): _description_ The hours specified for some of the services
            require_part (_type_): _description_ The prat required for that specific service
        """
        self.ID = ID
        self.name = name
        self.cost_per_hour = cost_per_hour
        self.require_user_input_hour = require_user_input_hour
        self.service_hour = service_hour
        self.require_part = require_part
        
    # function to calculate the service cost         
    def compute_service_cost(self):
        return self.cost_per_hour * self.service_hour

    # function to set the service hour for services that require user input hour    
    def set_service_hour(self, user_service_hr):
        self.service_hour = user_service_hr   
                   
    def display_info(self):
        print(f'ID: {self.ID}, name: {self.name}, cost per hour: {self.cost_per_hour}, user input hour: {self.require_user_input_hour}, service hour: {self.service_hour}, require part: {self.require_part}')   

class Part:
    """_summary_ This class defines the structure of part objects
    """
    def __init__(self, ID, name, price):
        """_summary_
        This method is the constructor of the Part class
        Args:
            ID (_type_): _description_ ID of the part
            name (_type_): _description_ The name of the part
            price (_type_): _description_ The price of the part
        """
        self.ID = ID
        self.name = name
        self.price = price
    
    def display_info(self):
        print(f'ID: {self.ID}, name: {self.name}, price: {self.price}')

class Records:
    def __init__(self):
        # creating the list methods for the existing customers, services and parts
        self.existing_customers = []
        self.existing_services = []
        self.existing_parts = []
                
        self.read_customers()  
        self.read_services()   
        self.read_parts() 
    
    def read_customers(self):
        """_summary_
        This method reads the customer file and 
        creates customer objects from the repective customer type classes
        i.e. Customer, Member and Premium Member and 
        adds those customers to the existing customers list
        """
        file = open("customers.txt")
        for line in file:
            line = line.split(',')
            ID = line[0].strip() 
            name = line[1].strip()
            if line[2].strip().lower() != "na": 
                discount_rate = float(line[2].strip())
            if line[3].strip().lower() != "na": 
                service_credit = int(line[3].strip())
            # checking the beginging of the ID to know which class the customer belongs to 
            if ID[0] == "C":
                cutomer = Customer(ID, name)
                self.existing_customers.append(cutomer)
            elif ID[0] == "M":
                member = Member(ID, name)
                self.existing_customers.append(member)
            elif ID[0] == "P":
                premium_mem = PremiumMember(ID, name, service_credit, discount_rate)
                self.existing_customers.append(premium_mem)
    
    def read_services(self):
        """_summary_
        This method reads the services file and 
        creates a service object from the service class and 
        adds those services to the existing services list
        """
        file = open("services.txt")
        for line in file:
            line = line.split(',')
            # ensuring each of the values in the line is stripped of extra characters
            ID = line[0].strip()
            if ID[:2] == "SP": # then it is a service package
                package_name = line[1]
                service_names = line[2:]
                # create a servicePacakge Obj
                packages = ServicePackage(ID, package_name, service_names)
                self.existing_services.append(packages)
            else:
                name = line[1].strip()
                cost = float(line[2].strip())
                input_hr = line[3].strip()
                if line[4].strip().lower() != "na": 
                    service_hour = float(line[4].strip())
                require_part = line[5].strip()
            
                service = Service(ID, name, cost, input_hr, service_hour, require_part)
                self.existing_services.append(service)
        
        for service in self.existing_services:
            if isinstance(service, ServicePackage):
                service_objects = [] # the list of the services in the service package as objects
                for service_name in service.list_of_services:
                    service_obj = self.find_service(service_name)
                    service_objects.append(service_obj)
                service.list_of_services = service_objects # so the list is of service objects
    
    def read_parts(self):
        """_summary_
        reads in the list 
        then with each line you create a part object 
        then add this new part object into the list of parts
        """
        file = open("parts.txt")
        for line in file:
            line = line.split(',')
            ID = line[0].strip() 
            name = line[1].strip()
            price = float(line[2].strip())
            part = Part(ID, name, price)
            self.existing_parts.append(part)
            
    def _find(self, search_key, attribute_list):
        key_type = "name" if search_key.isalpha() else "ID"
        for  attribute in attribute_list:
            if key_type  == "name" and attribute.name.lower() == search_key.lower():
                return attribute
            elif key_type  == "ID" and attribute.ID.lower() == search_key.lower():
                return attribute
        return None
         
    # this method will call the find method and pass in the search key and the customer list      
    def find_customer(self, search_key):
        return self._find(search_key, self.existing_customers)

    # this method will call the find method and pass in the search key and the services list      
    def find_service(self, search_key):
        return self._find(search_key, self.existing_services)
    
    # this method will call the find method and pass in the search key and the parts list      
    def find_part(self, search_key):
        return self._find(search_key, self.existing_parts)   
            
    def list_customers(self):
        """_summary_
             This Method calls the display info method of the customers classes
        """
        for customer in self.existing_customers:
            customer.display_info()
    
    def list_services(self):
        """_summary_
             This Method calls the display info method of the service class
        """
        for service in self.existing_services:
            service.display_info() 
    
    def list_parts(self):
        """_summary_
        This Method calls the display info method of the part class
        """
        # Go through the existing parts list and print the information
        for part in self.existing_parts:
            part.display_info()
    
class ServiceJob:
    # method is the constructor of the class servicejob
    def __init__(self, customer, service, part):
        self.customer = customer
        self.service = service
        self.part = part
        
    # method returns the o.g. cost, the total cost and the service credit for premium members  
    def compute_cost(self):
        original_cost = 0.0
        discount = 0.0
        total_cost = 0.0
        service_credit = 0
        part_cost = 0.0
        service_cost = self.service.compute_service_cost()
        
        # check if there's a part added to the service
        if self.part:
                part_cost = self.part.price # change part cost
                
        original_cost = service_cost + part_cost # add the part cost to the total
         
        if isinstance(self.customer, Member): # check to see if the customer is a Member
            discount = self.customer.get_discount(service_cost) # get the member discount
            total_cost = service_cost - discount
            
        total_cost = original_cost - discount   
            
        if isinstance(self.customer, PremiumMember):
             service_credit = self.customer.get_credit(total_cost) # we get the credit which will return the credit they've earned for this transaction
             self.customer.update_credit(service_credit) # update their total credits
                
        return original_cost, discount, total_cost, service_credit
    
class ServicePackage:  
    # method is the constructor of the class servicejob
    def __init__(self, ID, name, list_of_services):
        self.ID = ID
        self.name = name
        self.list_of_services = list_of_services
        
    def compute_cost(self, customer, parts):
        services_cost = 0.0
        parts_cost = 0.0
        total_cost = 0.0
        discount = 0
        service_credit = 0
        
        # get the total for all the services in the package
        for service in self.list_of_services:
            services_cost += service.compute_service_cost()
            
        # get the total for all the parts in the respective packages   
        for part in parts:
            if part:
                parts_cost += part.price
                
        original_cost = services_cost  + parts_cost
        
        cost_after_discount = services_cost * 0.75  # calcuate the discount from the service total

        if isinstance(customer, Member): # check to see if the customer is a Member
            discount = customer.get_discount(cost_after_discount) # get the member discount
            
        total_cost = cost_after_discount - discount + parts_cost
            
        if isinstance(customer, PremiumMember):
            service_credit = customer.get_credit(total_cost) # we get the credit which will return the credit they've earned for this transaction
            customer.update_credit(service_credit) # update their total credits
        
        return original_cost, discount, total_cost, service_credit
        
    def display_info(self):    
        print(f'ID: {self.ID}, name: {self.name}, {", ".join(self.list_of_services.names)}')     
    
# functions takes in records and creates a new ID that is unquie for new customers
def set_newID(records):
    all_id_nums = [] # list of all the existing ID numbers
    for customers in records.existing_customers:
        customer_id = customers.get_ID() # return the customer's id
        ID_num = int(customer_id[1:]) # the id's of each customer
        all_id_nums.append(ID_num) # all the ID numbers
    max_id_num = max(all_id_nums)
    ID = "C" + str(int(max_id_num) + 1) # always add one to whatever the max num is for the new customer ID
    return ID

# this method will create a service job and also perfrom most of the 
# user input interactions with the system
def perform_service(records):
    new_member = False
   
    customer_name = check_name()

    # check if they are an existing customer    
    customer = records.find_customer(customer_name)
    # if they don't exist in the customer list we create a customer object
    if not customer: 
        new_member = True
        ID = set_newID(records)
        customer = Customer(ID, customer_name)
    
    service = check_service(records) # check if the service entered is correct
    
    # providing checks and getting user inputs for the service packages where it is required
    if isinstance(service, ServicePackage): # check if the service is a service package
        required_parts = []
        for service_obj in service.list_of_services:
            if service_obj.require_user_input_hour == "yes": # does the user have to enter the service hours
                num_hours = check_user_service_hr()
                service_obj.set_service_hour(num_hours)
            part = None
            if service_obj.require_part == "yes": # if user has to specify the required service part
                part = check_valid_part(records)
                required_parts.append(part)
                
        original_cost, discount, total_cost, service_credit = service.compute_cost(customer, required_parts)        
    else:        
        if service.require_user_input_hour == "yes": # does the user have to enter the service hours
            num_hours = check_user_service_hr()
            service.set_service_hour(num_hours) # setting the entered and valid user hour

        part = None
        if service.require_part == "yes": # if user has to specify the required service part
            part = check_valid_part(records)
    
        #Instantiate the servicejob class and create a servicejob object which is the cost of the service
        service_job = ServiceJob(customer, service, part) 
        original_cost, discount, total_cost, service_credit = service_job.compute_cost()
    
    # new member registration
    if new_member:
        current_id = customer.get_ID()
        current_id_num = current_id[1:]
        #member_status = customer
        customer_response = input("Would you like to be a member or just a customer? enter yes/no\n")
        if customer_response == "yes":
            customer = Member("M" + current_id_num, customer_name)
            member_response_P = input("Would you like to be a standard or premium member? enter yes/no\n")
            if member_response_P == "yes":
                customer = PremiumMember("P" + current_id_num, customer_name, 0)
                
        # update records i.e. members file and the existing_members list
        records.existing_customers.append(customer)
        with open("customers.txt", 'a') as file:
            if customer and isinstance(customer, PremiumMember):
                file.write(f'\n{customer.get_ID()}, {customer_name}, {customer.get_discount_rate()}, {customer.service_credit}')
            elif customer and isinstance(customer, Member):
                file.write(f'\n{customer.get_ID()}, {customer_name}, {customer.get_discount_rate()}, na')
            else:
                file.write(f'\n{customer.get_ID()}, {customer_name}, na, na')
        file.close()        

    part_cost = 0.0
    part_name = None
    if part:
        part_cost = part.price
        part_name = part.name

    # create the reciept
    if isinstance(customer, PremiumMember):
        # call print method that has credit and registration cost
        print_receipt_P(service.name, service.service_hour, part_name, part_cost, original_cost, discount, total_cost, service_credit, new_member)
    elif isinstance(service, ServicePackage):
        print_receipt_SV(service, required_parts, original_cost, discount, total_cost, service_credit, new_member)
    else:
        # call regular print method
        print_receipt(service.name, service.service_hour, part_name, part_cost, original_cost, discount, total_cost)
  
# This method prints receipts for the premium members
def print_receipt_P(service_name, service_hr, part_name, part_cost, original_cost, discount, total_cost, service_credit, new_member):
    """_summary_
Args:
    service_name (_type_): _description_ Name of the service the customer requested
    service_hr (_type_): _description_ Service hours entered by the customer
    part_name (_type_): _description_ Name of the part required by the customer
    part_cost (_type_): _description_ The price of the part
    total (_type_): _description_ The total for the customer's order
    discount (_type_): _description_ The discount amount applied to the customers order
"""
    print("-"*60 + "\n" + "\t"*3 +"Receipt")
    print("-"*60)
    print(service_name + ":" + "\t"*5 + f"{service_hr}" + " x 40/hour")
    if part_name is not None:
        print(part_name + ":" +"\t"*6 + f"{part_cost:.2f}")
    print("-"*60)
    print("Original cost:"+"\t"*5 + f"{original_cost:.2f}" +" (AUD)") 
    print("Discount:"+"\t"*5 + f"{discount:.2f}" + " (AUD)")
    if new_member:
        print("Registration cost:"+"\t"*4 + f"{50:.2f}" + " (AUD)")
        total_cost += 50 # add the registration cost to the total
    print("Total cost:"+"\t"*5 + f"{total_cost:.2f}" + " (AUD)")  
    print("Credit:"+"\t"*6 + f"{service_credit:.2f}" + " (AUD)\n")  
     
def print_receipt(service_name, service_hr, part_name, part_cost, original_cost, discount, total_cost):
    """_summary_
Args:
    service_name (_type_): _description_ Name of the service the customer requested
    service_hr (_type_): _description_ Service hours entered by the customer
    part_name (_type_): _description_ Name of the part required by the customer
    part_cost (_type_): _description_ The price of the part
    total (_type_): _description_ The total for the customer's order
    discount (_type_): _description_ The discount amount applied to the customers order
"""
    print("-"*60 + "\n" + "\t"*3 +"Receipt")
    print("-"*60)
    print(service_name + ":" + "\t"*5 + f"{service_hr}" + " x 40/hour")
    if part_name is not None:
        print(part_name + ":" +"\t"*6 + f"{part_cost:.2f}")
    print("-"*60)
    print("Original cost:"+"\t"*5 + f"{original_cost:.2f}" +" (AUD)") 
    print("Discount:"+"\t"*5 + f"{discount:.2f}" + " (AUD)")
    print("Total cost:"+"\t"*5 + f"{total_cost:.2f}" + " (AUD)\n")  

# This method prints the receipt for the service packages
def print_receipt_SV(service_package, required_parts, original_cost, discount, total_cost, service_credit, new_member):
    """_summary_
Args:
    service_name (_type_): _description_ Name of the service the customer requested
    service_hr (_type_): _description_ Service hours entered by the customer
    part_name (_type_): _description_ Name of the part required by the customer
    part_cost (_type_): _description_ The price of the part
    total (_type_): _description_ The total for the customer's order
    discount (_type_): _description_ The discount amount applied to the customers order
"""
    print("-"*60 + "\n" + "\t"*3 +"Receipt")
    print("-"*60)
    print(service_package.name)
    for service in service_package.list_of_services:
        for part in required_parts:
            print(service.name + ":" + "\t"*5 + f"{service.service_hour}" + " x 40/hour")
            if part:
                print(part.name + ":" +"\t"*6 + f"{part.price:.2f}")
    print("-"*60)
    print("Original cost:"+"\t"*5 + f"{original_cost:.2f}" +" (AUD)") 
    print("Discount:"+"\t"*5 + f"{discount:.2f}" + " (AUD)")
    if new_member:
        print("Registration cost:"+"\t"*4 + f"{50:.2f}" + " (AUD)")
        total_cost += 50 # add the registration cost to the total
    print("Total cost:"+"\t"*5 + f"{total_cost:.2f}" + " (AUD)")  
    if service_credit:
        print("Credit:"+"\t"*6 + f"{service_credit:.2f}" + " (AUD)\n")  
    
class MainErrorClass(Exception):
    pass    

class CustomerNameError(MainErrorClass):
    pass

# validate customer name
def check_name():
    # continues looping until the name is valid
    while True:
        try:
            customer_name = input("Hello there! Please enter the name of the customer:\n").lower()
            if not customer_name.isalpha():
                raise CustomerNameError("Error detected, name entered contains non-alphabetic characters")
            return customer_name # returns a valid customer name 
        except CustomerNameError as error:
            print(error)
        customer_name = input("Please enter customer name with only alphabetic characters\n")
    
class ServiceNameError(MainErrorClass):
    pass

# validate entered service
def check_service(records):
    while True:
        try:
            service_requested = input("Please enter the service requested by the customer:\n")
            service = records.find_service(service_requested)
            if not service:
                raise ServiceNameError("Error detected, invalid service entered")
            return service
        except ServiceNameError as error:
            print(error)
            
class UserServiceHourError(MainErrorClass):  
    pass

# validate user entered service hours
def check_user_service_hr():
    while True:
        try:
            num_hours = input("Please enter number of service hours required:\n") # get user service hours if the user has to input them
            num_hours = float(num_hours)
            if (num_hours % 0.5) != 0 or num_hours < 1:
                raise UserServiceHourError("Error detected, invalid service hours")  
            return num_hours 
        except UserServiceHourError as error:
                print(error)
        except ValueError:
                print("Error, numerical value required here")
      
class PartNameError(MainErrorClass):
    pass

# validate the entered part    
def check_valid_part(records): 
    while True:
        try:
            part_required = input("Please enter the part required for this service:\n")
            part = records.find_part(part_required)
            if not part: 
                raise PartNameError("Error detected, invalid part entered")  
            return part
        except PartNameError as error:
            print(error)  
              
def update_services(services):
    """_summary_ This method updates the services specifications

    Args: 
        services (_type_): _description_ The dictionary of the services provided
        and their specifications
    """
    service_change = input("\nPlease enter the service and the service update you wish to make\n")
    service_change = service_change.split(',')
    service_name = service_change[0].strip() 
    service_hour = service_change[1].strip()
    if service_name in services:
        if service_hour == "na":
            services[service_name]["req_input_hours"] = "yes"
        else: 
             services[service_name]["service_hours"] = float(service_hour)    
    
def update_parts(part_prices):
    """_summary_ This method updates the parts and adds their
    respective specifications

    Args:
        part_prices (_type_): _description_ The dictionary for the parts and 
        their respective prices
    """
    update_choice = input("Do you want to add or remove a part? 'a' to add and 'r' to remove\n")
    if update_choice == "a":
        new_part = input("Enter the part and its price in the format: part1, price1 etc\n")
        part_and_price = new_part.split(",") 
        for x in range(0, len(part_and_price), 2):
            part_and_price[x] = part_and_price[x].strip()
            # if the value is in the part dictionary already then only edit the price otherwise add new element to the dictionary
            if part_and_price[x] in part_prices.keys(): # if it is a key of the dictionary then its a part
                part_prices[part_and_price[x]] = float(part_and_price[x+1]) # change only the price 
            else:
                # I am assumming the user will always input a part and its price
               part_prices.update({part_and_price[x]: float(part_and_price[x+1])}) 
    elif update_choice == "r":
        remove_part = input("Enter part/parts to remove\n")
        parts_and_prices = remove_part.split(",") 
        for parts in parts_and_prices:
            parts = parts.strip()
            if parts in part_prices:
                del part_prices[parts]
    else:
        print("enter 'a' to update and 'r' to remove")    
    
class Main:
    
    def __init__(self):
       pass  
        
    def run(self):
        """_summary_ This method contains the menu options and the 
        whole program is run from this method
        """
        present_files = []
        required_files = ["customers.txt", "parts.txt", "services.txt"]
        script_directory = os.path.dirname(os.path.abspath(__file__)) # Here I am making sure to look into the folder where the .py file is                
        for item in os.listdir(script_directory):
            if os.path.isfile(os.path.join(script_directory, item)): # check if it is a file i.e. .txt file
                present_files.append(item) # adds the file to the present files list
                    
        for file in required_files:
            if file not in present_files: 
                print(f'{file} is missing, so the program has been terminated')  
                sys.exit() # to terminate the program when a file is missing
                
        # Instantiate the record class and create a record object
        records = Records()
        
        while True:
        # run the menu at least once 
         
            menu = """
            1. Display existing customers
            2. Display existing services
            3. Display existing parts
            4. Perform a service
            5. Exit the program
            """
            
            print("\nWelcome to the repair store") 
            print('#'*50)
            print(menu)
            print(50*"#")
            
            user_choice = input("Please select an option from the menu above\n")
            
            # Calls the repective list methods for each option
            if user_choice == "1":
                records.list_customers()
            elif user_choice == "2":
                records.list_services()
            elif user_choice == "3":
                records.list_parts()
            elif user_choice == "4":
                perform_service(records)
            elif user_choice == "5":
                update_services()
            elif user_choice == "6":
                update_parts()
            #elif user_choice == "7":
                #display_service_jobs()
                
            if user_choice == "8":
                break
                     
        
if __name__ == "__main__":
    program = Main()
    program.run()
    
# Citations