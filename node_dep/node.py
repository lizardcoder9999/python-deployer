import paramiko
import os
import pysftp

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
        username,password = self.server.user,self.server.password
        makedir_sh_dir = os.path.dirname(os.path.realpath('__file__'))
        makedir_sh_name = os.path.join(makedir_sh_dir,"scripts/jsnode/makedir.sh")
        script_server_path = f"{self.path}/scripts"
        with pysftp.Connection(self.server.host, username=username, password=password) as sftp:
            sftp.mkdir(self.server.project,mode=777)
            sftp.mkdir('scripts',mode=777)
            sftp.chdir(f'{self.path}/scripts')
            sftp.put(makedir_sh_name,os.path.join("","makedir.sh"))
   

    def make_dir(self):
        makedir_sh_dir = os.path.dirname(os.path.realpath('__file__'))
        makedir_sh_name = os.path.join(makedir_sh_dir,"scripts/jsnode/makedir.sh")
        with open(makedir_sh_name, 'w') as f:
            data = f"sudo su \n{self.server.user}\n{self.server.password}\nmkdir {self.server.project}\nchmod -R 777 {self.server.project}"
            f.write(data)
    
        (stdin, stdout, stderr) = self.session.exec_command("pwd",get_pty=True)
        for line in stdout.read().splitlines() :
            formatted_line = line.decode("utf-8")
            print(formatted_line)
            self.path = str(formatted_line)
            break
       

    
    

        

        
            






    
    