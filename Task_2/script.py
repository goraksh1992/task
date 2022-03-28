from time import sleep
import paramiko
import os 


class ServerExample:

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
    
    def connect(self):
        router=self.hostname
        conn = paramiko.SSHClient()
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        conn.connect(router, username=self.username, password=self.password)

        return conn

    
    def run_command(self, command):
        try:
            conn = self.connect()
            router_conn = conn.invoke_shell()

            # Command
            router_conn.send(f'{command} \n')
            sleep(1)
            
            data = router_conn.recv(5000).decode("utf-8")

            # Save Response in file
            with open('output.txt', "a") as f:
                f.write(str(data))

            print(f"Output of { command } store in output.txt file")
        
        except Exception as e:
            print(e)

        conn.close()

    
    def transfer_file(self, source, destination):
        try:
            _, tail = os.path.split(source)
            conn = self.connect()
            sftp_client = conn.open_sftp()
            sftp_client.put(source, destination+f"/{tail}")

            print("File Transfer")
        
        except Exception as e:
            print(e)

        sftp_client.close()
        conn.close()


if __name__ == "__main__":
    obj = ServerExample("host", "username", "password")
    option = input("""
    1. SSH to the server. Run a command(ls) on the server and save its output to an external text file \n
    2. File transfer to the server(FTP) \n 
    Enter your Choice:  """)
    if option == '1':
        command = input("Enter command: ")
        obj.run_command(command)
    elif option == '2':
        source = input("Enter source file path: ")
        destination = input("Enter destination path: ")

        obj.transfer_file(source, destination)
    
    else:
        print("Please enter valid option")

