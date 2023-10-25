############
## CLIENT ##
############

import ssl
import socket 
import hashlib
import math
import random
from sympy import isprime

#Server Settings
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

#Creating a Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

while True: 
    print("+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("Enter clients message: ") 
    print("+=+=+=+=+=+=+=+=+=+=+=+=+")
    message = input()
    if message == 'quit':
        break

    #Exchange
    #client hello
    
    #send message to the server
    client_socket.send(message.encode())

    #receiev message from server
    reponse = client_socket.recv(1024).decode()

    #Calculate public key and send to server

    #Receive servers public key in plain text

    #Calculate shared secret key

    print(f"Received message from server:{reponse}")

client_socket.close()