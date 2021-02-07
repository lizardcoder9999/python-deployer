import paramiko

class Node: 
    def __init__(self,server,path=""):
        self.server = server
        self.path = path
        self.session = paramiko.SSHClient()
       

    def establish_connection(self):
        port = 22
        self.session.load_system_host_keys()
        self.session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.session.connect(self.server.host,port,self.server.user,self.server.password)

    def establish_sftp(self):
        port = 22 
        host,port = self.server.host,port
        transport = paramiko.Transport((host,port))
        username,password = self.server.user,self.server.password
        transport.connect(None,username,password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        #Upload
        filepath = f"{self.path}/{self.server.project}"
        localpath = self.server.project_path
        sftp.put(localpath,filepath)

        if sftp: sftp.close()
        if transport: transport.close()

    def make_dir(self):
        self.session.exec_command("sudo su")
        self.session.exec_command(self.server.user)
        self.session.exec_command(self.server.password)
        self.session.exec_command(f"mkdir {self.server.project}")
        self.session.exec_command(f"cd {self.server.project}")
        (stdin, stdout, stderr) = self.session.exec_command(f"pwd")
        for line in stdout.read().splitlines() :
            self.path = str(line)
            break


        
            






    
    