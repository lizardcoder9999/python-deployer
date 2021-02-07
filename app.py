import os 
import sys 
import base64
import paramiko
from cli.cli import Server
from node_dep.node import Node

print("This currently works for servers running Ubuntu and Debian based linux distrobutions")
print("Select one of the options below")
print("(1) Node Js")


user_selected = input("Select one of the options above: ")
converted_selected = str(user_selected)

# try:
if converted_selected == "1":
    print("(1) Web App")
    print("(2) Api")

    project_type = input("Selection: ")
    converted_project = str(project_type)

else : 
    print("You need to choose an option")

if converted_project == "1":
    serverObject = Server()
    serverObject.get_host()
    serverObject.get_user()
    serverObject.get_password()
    # client = SSHClient()
    # client.connect(serverObject.host, serverObject.user, serverObject.password)
    node = Node(serverObject)
    node.establish_connection()
    

     
# except: 
#     print("An Error has occured please try again")
    
    
