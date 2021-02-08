class Server:
    def __init__(self):
        self.question = "Enter your server info"
        self.host = ""
        self.user = ""
        self.password = ""
        self.project = ""
        self.project_path = ""
        self.project_entry = ""

        print("Please Enter your server info")

    def get_project_name(self):
        self.project = str(input("Please enter your project name: "))

    def get_project_path(self):
        self.project_path = str(input("Please enter your project path: "))

    def get_entry_point(self):
        self.project_entry = str(input("Please enter your entry point: "))

    def get_host(self):
        self.host = str(input("Please enter the host of your server: "))

    def get_user(self):
        self.user = str(input("Enter the username for your server: "))

    def get_password(self):
        self.password = str(input("Enter the password for your server: "))
    

        