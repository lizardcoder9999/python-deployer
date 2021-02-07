import paramiko

class Node: 
    def __init__(self,server):
        self.server = server

    def establish_connection(self):
        port = 22
        client = paramiko.SSHClient()
        client.load_system_host_keys()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(self.server.host,port,self.server.user,self.server.password)
    
        # (stdin, stdout, stderr) = client.exec_command



    
