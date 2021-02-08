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
        deployment_sh_dir = os.path.dirname(os.path.realpath('__file__'))
        deployment_sh_name = os.path.join(deployment_sh_dir,"scripts/jsnode/deployment.sh")
        user_zip_file = self.server.project_path
        script_server_path = f"{self.path}/scripts"
        with pysftp.Connection(self.server.host, username=username, password=password) as sftp:
            sftp.mkdir(self.server.project,mode=777)
            sftp.mkdir('scripts',mode=777)
            sftp.chdir(f'{self.path}/scripts')
            sftp.put(deployment_sh_name,os.path.join("","deployment.sh"))
            sftp.chdir(f'{self.path}/{self.server.project}')
            sftp.put(user_zip_file,os.path.join("",f"{self.server.project}.zip"))
   

    def make_dir(self):
        deployment_sh_dir = os.path.dirname(os.path.realpath('__file__'))
        deployment_sh_name = os.path.join(deployment_sh_dir,"scripts/jsnode/deployment.sh")
        with open(deployment_sh_name, 'w') as f:
            data = f"sudo su\n{self.server.user}\n{self.server.password}\ncurl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash\napt install nodejs\napt install unzip\nunzip -q {self.server.project}.zip\nnpm install\nnpm i pm2 -g\npm2 start {self.server.project_entry}\npm2 startup ubuntu\nufw enable\nufw status\nufw allow ssh\nufw allow http\nufw allow https\napt install nginx"
            f.write(data)
    
        (stdin, stdout, stderr) = self.session.exec_command("pwd",get_pty=True)
        for line in stdout.read().splitlines() :
            formatted_line = line.decode("utf-8")
            self.path = str(formatted_line)
            break

        def run_deploy_script(self):
            (stdin,stdout,stderr) = self.ession.exec_command("./scripts/deployment.sh")
            for line in stdout.read().splitlines():
                formatted_results = line.decode("utf-8")
                print(formatted_results)
            
       

    
    

        

        
            






    
    