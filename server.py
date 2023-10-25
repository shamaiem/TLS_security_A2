############
## SERVER ##
############

import ssl
import socket 
import hashlib
import math
#import cryptography
#import PyCryptodome

#Server Settings
HOST = 'localhost'
PORT = 12345

#Creating a Socket
#AF_INET specifies IPv4 address fam
#SOCK_STREM is for TCP oriented communication
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))

#Listen for incoming connections
server_socket.listen(1)

print(f"Server is listening on {HOST}:{PORT}")

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    #Establish key exchange
    #server hello

    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Received from client: {data}")

        # Respond to the client
        print("//\\//\\//\\//\\//\\//\\//\\")
        print("Enter server's response: ")
        print("//\\//\\//\\//\\//\\//\\//\\")
        response = input()
        client_socket.send(response.encode())

        
        #Calculate public key and send to client

        #Receive clients public key in plain text

        #Calculate shared secret key

    client_socket.close()

# if __name__ == '__main__':
#     m=0
#     b=0
#     print("I am in main")
#     check()