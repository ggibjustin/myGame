list_of_users = [] # Will display a list containing a dictionary in which the first value is the username and second
                   # will be the password

class Person:

    # Variables declared inside the class will be applied to all objects/members of the class
    
    def __init__(self, username, password, email_address):
        # Variables declared inside the instantiation and will only be applies to instance created
        self.username = username
        self.password = password
        self.email_address = email_address
        self.displayed_location = "optional"
        self.address = "optional"
        self.city = "optional"
        self.state = "optional"
        list_of_users.append({self.username : self.password})
       
    def add_location(self,location):
        self.displayed_location = location

    def add_address(self,address, city, state):
        self.address = address
        self.city = city
        self.state = state

####################### End of class Definition ###############################

me = Person('ggibjustin','8589Gj00','ggibjustin@gmail.com')
kevin = Person('jpl.lineman','1Whalebone','jpl.lineman@gmail.com')
