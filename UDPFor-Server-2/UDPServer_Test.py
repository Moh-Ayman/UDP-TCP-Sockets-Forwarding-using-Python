import datetime
import socket
BindIP    = ""
MNGPort  = 50001
TranPort=60001
DTPort = 60002
bufferSize = 1024
EndPointPort=<IP>
EndPointIP=<IP>

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
def Main():
	try:
		alog(" - Main() -- Started Successfully","s")
        
		alog(" - Main() -- Create a stream socket for MNGPort","n")
		s = socket.socket()
	       	alog(" - Main() -- Binding Server Address: "+str(BindIP)+" and Port: "+str(MNGPort),"n")
		s.bind((BindIP,MNGPort))
	        alog(" - Main() -- Enabling Listing","n")
		s.listen(1)

	        alog(" - Main() -- Create a datagram socket for Data Port","n")
		UDPServerSocket_D = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	        alog(" - Main() -- Binding Localhost and Data Port: "+str(DTPort),"n")
		UDPServerSocket_D.bind((BindIP, DTPort))

	        alog(" - Main() -- Create a datagram socket for Transaction Port","n")
		UDPServerSocket_T = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
	        alog(" - Main() -- Binding Localhost and Transaction Port: "+str(TranPort),"n")
		UDPServerSocket_T.bind((BindIP, TranPort))

	        alog(" - Main() -- Starting While()","n")
		while(True):
	                alog(" - Main() - SendTransactionId() -- Openning Transaction Log ","n")
       		        fileHandle = open ( 'UDPServer_Transactional.log',"a+" )
	                HN = socket.gethostname()

		        alog(" - Main() -- Start Recieving Transaction Data","n")
	    		bytesAddressPair_T = UDPServerSocket_T.recvfrom(bufferSize)
	                alog(" - Main() -- Extracting MSG from recieved data","n")
	    		message_T = bytesAddressPair_T[0]
	                alog(" - Main() -- Extracting Address from recieved data","n")
	    		address_T = bytesAddressPair_T[1]
	                alog(" - Main() -- Formating MSG","n")
	    		clientMsg_T = "Message from Client:{}".format(message_T)
	                alog(" - Main() -- Formatted MSG: \n"+str(clientMsg_T),"n")
	                alog(" - Main() -- Formating Address","n")
	    		clientIP_T  = "Client IP Address:{}".format(address_T)
	                alog(" - Main() -- Formatted Address: \n"+str(clientIP_T),"n")
    			print(clientMsg_T)
    			print(clientIP_T)
			ID=message_T.split(",")[1]
			alog(" - Main() - SendTransactionId() -- TranId is: "+"\n"+str(format_time())+","+str(ID)+","+str(address_T[0])+","+str(HN)+",Recieving,Before Recieving Data","n")
                        fileHandle.write("\n"+str(format_time())+","+str(ID)+","+str(address_T[0])+","+str(HN)+",Recieving,Before Recieving Data")


	                alog(" - Main() -- Start Recieving Data","n")
	    		bytesAddressPair_D = UDPServerSocket_D.recvfrom(bufferSize)
	                alog(" - Main() -- Extracting MSG from recieved data","n")
	    		message_D = bytesAddressPair_D[0]
	                alog(" - Main() -- Extracting Address from recieved data","n")
	    		address_D = bytesAddressPair_D[1]
	                alog(" - Main() -- Formating MSG","n")
	    		clientMsg_D = "Message from Client:{}".format(message_D)
	                alog(" - Main() -- Formatted MSG: \n"+str(clientMsg_D),"n")
	                alog(" - Main() -- Formating Address","n")
	    		clientIP_D  = "Client IP Address:{}".format(address_D)
	                alog(" - Main() -- Formatted Address: \n"+str(clientIP_D),"n")
    			print(clientMsg_D)
    			print(clientIP_D)

			alog(" - Main() -- Start Recieving Transaction Data","n")
	    		bytesAddressPair_T = UDPServerSocket_T.recvfrom(bufferSize)
	                alog(" - Main() -- Extracting MSG from recieved data","n")
	    		message_T = bytesAddressPair_T[0]
	                alog(" - Main() -- Extracting Address from recieved data","n")
	    		address_T = bytesAddressPair_T[1]
	                alog(" - Main() -- Formating MSG","n")
	    		clientMsg_T = "Message from Client:{}".format(message_T)
	                alog(" - Main() -- Formatted MSG: \n"+str(clientMsg_T),"n")
	                alog(" - Main() -- Formating Address","n")
	    		clientIP_T  = "Client IP Address:{}".format(address_T)
	                alog(" - Main() -- Formatted Address: \n"+str(clientIP_T),"n")
    			print(clientMsg_T)
    			print(clientIP_T)
                        ID=message_T.split(",")[1]
                        alog(" - Main() - SendTransactionId() -- TranId is: "+"\n"+str(format_time())+","+str(ID)+","+str(address_T[0])+","+str(HN)+",Recieving,After Recieving Data","n")
                        fileHandle.write("\n"+str(format_time())+","+str(ID)+","+str(address_T[0])+","+str(HN)+",Recieving,After Recieving Data")

                	fileHandle.close()
			if message_D:
	                	alog(" - Main() -- Creating a UDP Socket for sending data to EndPoint","n")
				sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
	                        alog(" - Main() -- Encoding Data","n")
	        		bytesToSend_EndPoint   = str.encode(message_D)
	                        alog(" - Main() -- Start Sending Data","n")
	        		sock.sendto(bytesToSend_EndPoint, (EndPointIP,EndPointPort))
	                        alog(" - Main() -- Data Sent Successfully","n")
	except (ValueError,IOError) as err:
		alog(" - Main() -- Error Occured \n"+str(err),"e")


with open ("UDPServer_Application.log",'a') as f:
    Main()
f.close()