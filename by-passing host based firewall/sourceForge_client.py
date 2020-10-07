import paramiko     
import scp         


ssh_client = paramiko.SSHClient()  

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


ssh_client.connect("web.sourceforge.net", username="isityou", password="YOUR_PASSWORD") 


scp = scp.SCPClient(ssh_client.get_transport())  

scp.put('C:/Users/saurabh/Desktop/buffer.c') 
print('[+] File is uploaded ')


scp.close()
print('[+] Closing the socket')