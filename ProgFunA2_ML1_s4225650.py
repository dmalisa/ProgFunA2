# Name: Denise Malisa
# Student_ID: s4225650

class Customer:
    """_summary_ This class defines the structure of a basic customer object
    with a ID and a name
    """
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name
        
    def display_info(self):
        print("ID: " + self.ID + ", name: " + self.name)

    
class Member:
    """_summary_ This class defines the structure of a member object 
    with the respective properties for a member
    """
    def __init__(self, ID, name, discount_rate):
        self.ID = ID
        self.name = name
        self.discount_rate = discount_rate
        
    def display_info(self):
        print("ID: " + self.ID + ", name: " + self.name + ", discount rate: " + self.discount_rate)
        

class PremiumMember:
    """_summary_ This class defines the structure of a premium member object 
    with the respective premium member attributes
    """
    def __init__(self, ID, name, discount_rate, service_credit):
        self.ID = ID
        self.name = name
        self.discount_rate = discount_rate
        self.service_credit = service_credit
    
    def display_info(self):
        print("ID: " + self.ID + ", name: " + self.name + ", discount rate: " + self.discount_rate 
              + ", service credit: " + self.service_credit)

    

class Service:
    """_summary_ This class defines the structure a service object with the respective 
    attributes required to represent a service
    """
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
        
    def display_info(self):
        print("ID: " + self.ID + ", name: " + self.name + ", cost per hour: " + self.cost_per_hour,
              ", user input hour: " + self.require_user_input_hour + ", service hour: " + self.service_hour
              + ", require part: " + self.require_part)
        
    

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
        print("ID: " + self.ID + ", name: " + self.name + ", price: " + self.price)

class Records:
    def __init__(self):
        # creating the list methods for the existing customers, services and parts
        self.existing_customers = []
        self.existing_services = []
        self.existing_parts = []
    
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
            discount_rate = line[2].strip()
            service_credit = line[3].strip()
            # checking the beginging of the ID to know which class the customer belongs to 
            if ID[0] == "C":
                cutomer = Customer(ID, name)
                self.existing_customers.append(cutomer)
            elif ID[0] == "M":
                member = Member(ID, name, discount_rate)
                self.existing_customers.append(member)
            elif ID[0] == "P":
                premium_mem = PremiumMember(ID, name, discount_rate, service_credit)
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
            name = line[1].strip()
            cost = line[2].strip()
            input_hr = line[3].strip()
            service_hour = line[4].strip()
            require_part = line[5].strip()
            
            service = Service(ID, name, cost, input_hr, service_hour, require_part)
            self.existing_services.append(service)
    
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
            price = line[2].strip()
            part = Part(ID, name, price)
            self.existing_parts.append(part)
            
    def list_customers(self):
        """_summary_
             This Method calls the display info method of the customers classes
        """
        self.read_customers()
        for customer in self.existing_customers:
            customer.display_info()
    
    def list_services(self):
        """_summary_
             This Method calls the display info method of the service class
        """
        self.read_services()
        for service in self.existing_services:
            service.display_info()
    
    def list_parts(self):
        """_summary_
        This Method calls the display info method of the part class
        """
        self.read_parts()
        # Go through the existing parts list and print the information
        for part in self.existing_parts:
            part.display_info()

class Main:
    
    def __init__(self):
       pass
    
    def run(self):
        """_summary_ This method contains the menu options and the 
        whole program is run from this method
        """
        
        while True:
        # run the menu at least once 
                    
            menu = """
            1. Display existing customers
            2. Display existing services
            3. Display existing parts
            4. Exit the program
            """
            
            print("\nWelcome to the repair store") 
            print('#'*50)
            print(menu)
            print(50*"#")
            
            user_choice = input("Please select an option from the menu above\n")

            records = Records()
            
            if user_choice == "1":
                records.list_customers()
            elif user_choice == "2":
                records.list_services()
            elif user_choice == "3":
                records.list_parts()
                
            if user_choice == "4":
                break
            
        
if __name__ == "__main__":
    program = Main()
    program.run()