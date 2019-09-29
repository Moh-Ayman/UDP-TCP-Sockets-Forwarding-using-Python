import socket
import time
import random
import datetime
remoteServer=[ "Server1" , "Server2" ]
Server_M_Port=50001
Server_T_Port=60001
Server_D_Port=60002

HOST=random.choice(remoteServer)
#print(HOST)

def format_time():
    try:
        t = datetime.datetime.now()
        s = t.strftime('%m-%d-%Y %H:%M:%S.%f')
        return s[:-3]
    except (ValueError,IOError) as err:
        alog(" - Main() -- Error Occured \n"+str(err),"e")

def alog(message,status):
    try:
        if status=="e":
                f.write(format_time() + " -0000 ERROR " + str(message)+"\n")
        elif status=="s":
                f.write(format_time() + " -0000 SUCCESS " + str(message)+"\n")
        elif status=="n":
                f.write(format_time() + " -0000 INFO " + str(message)+"\n")
        elif status=="w":
                f.write(format_time() + " -0000 WARNING " + str(message)+"\n")
    except (ValueError,IOError) as err:
        alog(" - Main() - alog() -- Error Occured \n"+str(err),"e")


def SendData(HOST,Server_D_Port):
	try:
		alog(" - Main() - SendData() -- Started Successfully","s")
                alog(" - Main() - SendData() -- Combining Server Address (Host): "+str(HOST)+" and Data Port: "+str(Server_D_Port),"n")
		serverAddressPort_D   = (HOST, Server_D_Port)
                alog(" - Main() - SendData() -- Create a UDP socket at client side For Data Port","n")
  		UDPClientSocket_D = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                alog(" - Main() - SendData() -- Intializing bufferSize=1024","n")
		bufferSize = 1024

                alog(" - Main() - SendData() -- Intializing Data Variable","n")
        	msgFromClient_D       = "Daaaaaaaaaaataaaaaaaaaaaaaa"
                alog(" - Main() - SendData() -- Encoding Data MSG","n")
        	bytesToSend_D         = str.encode(msgFromClient_D)
                alog(" - Main() - SendData() -- Sending Encoded Data to Server Address on Data Port","n")
        	UDPClientSocket_D.sendto(bytesToSend_D, serverAddressPort_D)
                alog(" - Main() - SendData() -- Data Sent Successfully","s")
	except (ValueError,IOError) as err:
		alog(" - Main() - SendData() -- Error Occured \n"+str(err),"e")

def PortScanner(HOST,Server_M_Port):
	try:
                alog(" - Main() - PortScanner() -- Started Successfully","s")
                alog(" - Main() - PortScanner() -- Getting Random Remote Host: "+str(HOST),"n")
		remoteServerIP  = socket.gethostbyname(HOST)
                alog(" - Main() - PortScanner() -- Creating a TCP socket at client side for MGMT Port: "+str(Server_M_Port),"n")
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                alog(" - Main() - PortScanner() -- Checking Availabilty of MGMT Port","n")
		result = sock.connect_ex((remoteServerIP, Server_M_Port))
                alog(" - Main() - PortScanner() -- Returning Results","n")
		return result
	except (ValueError,IOError) as err:
                alog(" - Main() - PortScanner() -- Error Occured \n"+str(err),"e")

def SendTransactionId(HOST,Server_T_Port,Status,newid):
	try:
		SourceHN = socket.gethostname()
		
		alog(" - Main() - SendTransactionId() -- Started Successfully","s")
                alog(" - Main() - SendTransactionId() -- Combining Server Address (Host): "+str(HOST)+" and Transaction Port: "+str(Server_T_Port),"n")
                serverAddressPort_T   = (HOST, Server_T_Port)
                alog(" - Main() - SendTransactionId() -- Create a UDP socket at client side For Transaction Port","n")
                UDPClientSocket_T = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
                alog(" - Main() - SendTransactionId() -- Intializing bufferSize=1024","n")
                bufferSize = 1024

                alog(" - Main() - SendTransactionId() -- Openning Transaction Log ","n")
                fileHandle = open ( 'UDPClient_Transactional.log',"a+" )
                alog(" - Main() - SendTransactionId() -- Readlines ","n")
                alog(" - Main() - SendTransactionId() -- TranId is: "+"\n"+str(format_time())+","+str(newid)+","+str(SourceHN)+","+str(HOST)+","+Status,"n")
                fileHandle.write("\n"+str(format_time())+","+str(newid)+","+str(SourceHN)+","+str(HOST)+","+Status)
                fileHandle.close()


                alog(" - Main() - SendTransactionId() -- Intializing TransactionID Variable","n")
                Id=str(format_time())+","+str(newid)+","+str(SourceHN)+","+str(HOST)+","+Status
                alog(" - Main() - SendTransactionId() -- Encoding Data MSG","n")
                bytesToSend_T = str.encode(Id)
                alog(" - Main() - SendTransactionId() -- Sending Encoded Data to Server Address on Transaction Port","n")
                UDPClientSocket_T.sendto(bytesToSend_T, serverAddressPort_T)
                alog(" - Main() - SendTransactionId() -- Transaction Sent Successfully","s")
		

        except (ValueError,IOError) as err:
                alog(" - Main() - SendTransactionId() -- Error Occured \n"+str(err),"e")

def Main():
	try:
                alog(" - Main() -- Started Successfully","s")
                alog(" - Main() -- Retrieving PortScanner() Results","n")
		result = PortScanner(HOST,Server_M_Port)
                alog(" - Main() -- Results Retrieved with value: "+str(result),"n")
		if result == 0:
        		#print "Port {}:    Open".format(Server_M_Port)
			x="Port {}:    Open".format(Server_M_Port)
			#print(x)
                        alog(" - Main() -- MGMT Port is Available "+x,"s")
			alog(" - Main() -- Sending Data","n")			
	                alog(" - Main() - SendTransactionId() -- Openning Transaction Log ","n")
        	        fileHandle = open ( 'UDPClient_Transactional.log',"r" )
               		alog(" - Main() - SendTransactionId() -- Readlines ","n")
               		lineList = fileHandle.readlines()
                	if (lineList[-1].split(",")[1].isdigit()):
                        	alog(" - Main() - SendTransactionId() -- Last Line is Digit","n")

                        	#print lineList[-1].split(",")[1]
                        	oldid=lineList[-1].split(",")[1]
                        	alog(" - Main() - SendTransactionId() -- Old Id is: "+str(oldid),"n")
                        	newid=int(oldid)+1
                        	alog(" - Main() - SendTransactionId() -- New Id is: "+str(newid),"n")
	
        	        else:
                	        alog(" - Main() - SendTransactionId() -- Last Line is not Digit","n")
                        	newid=1
                        	alog(" - Main() - SendTransactionId() -- New Id is: "+str(newid),"n")
                	fileHandle.close()

			SendTransactionId(HOST,Server_T_Port,"Sending,Before Sending Data",newid)
			SendData(HOST,Server_D_Port)
                        SendTransactionId(HOST,Server_T_Port,"Sending,After Sending Data",newid)
                        alog(" - Main() -- Data Sent Successfully","s")
	except (ValueError,IOError) as err:
                alog(" - Main() -- Error Occured \n"+str(err),"e")

with open ("UDPClient_Application.log",'a') as f:    
    Main()
f.close()

