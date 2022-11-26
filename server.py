import socket
import tqdm


server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((socket.gethostname(),9999))
# binding the socket to the local host. With socket we send and receive data, 
server.listen() # prepared to listen to everything

serversocket,address =server.accept()  #When a connection is received, store the value in client socket and store their source address in address
print(f"Connection from {address} has been established ! ")
serversocket.send(bytes("Welcome to the server!","utf-8"))
#Responding to make sure the connection is established


#Receiving file from server: 

file_name=serversocket.recv(1024).decode("utf-8")
print(f"The file : {file_name} has been received properly")
#We need a byte string in order to store the values of the file sent, we will continously update the file 
file_bytes= b""
#Setting a flag for end of transfer: 

file=open(file_name,"wb") ## Open a file with the name of the file passed , and then we will write into it any data bytes that we need 

Finished=False




while not Finished:
    data_received=serversocket.recv(1024)
    if file_bytes[-10:] == b"<40097236>":
        Finished = True
    else:
        file_bytes+=data_received


file.write(file_bytes[0:-10])






file.close()    #When done writing into it, close the file
serversocket.close()
server.close()