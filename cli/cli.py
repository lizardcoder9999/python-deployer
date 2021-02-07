class Server:
    def __init__(self):
        self.question = "Enter your server info"
        self.host = ""
        self.user = ""
        self.password = ""

        print("Please Enter your server info")


    def get_host(self):
        self.host = str(input("Please enter the host of your server: "))

    def get_user(self):
        self.user = str(input("Enter the username for your server: "))

    def get_password(self):
        self.password = str(input("Enter the password for your server: "))
    

        