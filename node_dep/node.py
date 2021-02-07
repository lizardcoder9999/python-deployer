import paramiko
import os

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
        # global channel = self.session.get_transport().open_session()
        # channel.invoke_shell()

    def establish_sftp(self):
        port = 22 
        host,port = self.server.host,port
        transport = paramiko.Transport((host,port))
        username,password = self.server.user,self.server.password
        transport.connect(None,username,password)
        sftp = paramiko.SFTPClient.from_transport(transport)

        makedir_sh_dir = os.path.dirname(os.path.realpath('__file__'))
        makedir_sh_name = os.path.join(makedir_sh_dir,"scripts/jsnode/makedir.sh")
        

        #Upload
        # filepath = f"{self.path}/{self.server.project}"
        script_server_path = f"{self.path}/scripts"
        # localpath = self.server.project_path
        # sftp.put(localpath,filepath)
        sftp.mkdir("scripts",777)
        sftp.put(makedir_sh_name,script_server_path)

        if sftp: sftp.close()
        if transport: transport.close()

    def make_dir(self):
        makedir_sh_dir = os.path.dirname(os.path.realpath('__file__'))
        makedir_sh_name = os.path.join(makedir_sh_dir,"scripts/jsnode/makedir.sh")
        with open(makedir_sh_name, 'w') as f:
            data = f"sudo su \n{self.server.user}\n{self.server.password}\nmkdir {self.server.project}\nchmod -R 777 {self.server.project}"
            f.write(data)
     


        # self.session.exec_command("sudo su",get_pty=True)
        # self.session.exec_command(self.server.user,get_pty=True)
        # self.session.exec_command(self.server.password,get_pty=True)
        # self.session.exec_command(f"mkdir {self.server.project}",get_pty=True)
        # self.session.exec_command(f"chmod -R 777 {self.server.project}",get_pty=True)
        # self.session.exec_command(f"cd {self.server.project}",get_pty=True)
        (stdin, stdout, stderr) = self.session.exec_command("pwd",get_pty=True)
        for line in stdout.read().splitlines() :
            print(line)
            self.path = str(line)
            break
       

    
    

        

        
            






    
    