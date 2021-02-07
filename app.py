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
    print("Choose an upload method")
    print("(1) Ftp using .zip file")
    print("(2) Github repository")
    upload_type = input("Selection: ")
    converted_upload_type =str(upload_type)
    if converted_upload_type == "1":
        server = Server()
        server.get_project_name()
        server.get_project_path()
        server.get_host()
        server.get_user()
        server.get_password()
        node = Node(server)
        node.establish_connection()
        node.make_dir()
        node.establish_sftp()
    else :
        print("You need to choose a upload type.")

  
# except: 
#     print("An Error has occured please try again")
    
    
