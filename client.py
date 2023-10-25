import socket
import encryption_module
import json

server_response = " "

# -------------------- FUNCTIONS ------------------ #

# Function to take input from the client
def client_input():
    print("+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("Enter client's message:")
    print("+=+=+=+=+=+=+=+=+=+=+=+=+")
    client_message = input()
    return client_message

def establish_client_handshake():
    # Exchange
    # "Client Hello" message
    client_message = "Client Hello!"
    print("Client sent first handshake with, ",client_message)
    client_socket.send(client_message.encode())

# ------------------- FUNCTIONS END ------------- #

# Server Settings
SERVER_HOST = 'localhost'
SERVER_PORT = 12345

# Creating a Socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((SERVER_HOST, SERVER_PORT))

establish_client_handshake()
server_response = client_socket.recv(1024).decode()
if server_response == "Server Hello!":
    print("Client received second handshake with, ", server_response)

    # ----------------------- ENCRYPTED COMMUNICATION ----------------- #
    # while True:
    #     client_message = client_input()

    #     # Send message to the server
    #     client_socket.send(client_message.encode())

    #     if client_message == 'quit':
    #         break

    #     # Receive message from the server
    #     server_response = client_socket.recv(1024).decode()

    #     # Calculate public key and send to the server
    #     # Receive the server's public key in plain text
    #     # Calculate the shared secret key

    #     print(f"Received message from server: {server_response}")
else:
    print("Three-Way Handshake Failed.")

private_key, public_key =encryption_module.RSAkeygeneration(8)
print(f"Server Public key {public_key}, Server Private Key {private_key}")

# Initializing certificate content
certificate_content = {
    'subject': 'client',
    'public_key': public_key
}

# Signing Certificate

json_string = json.dumps(certificate_content)
signature = encryption_module.create_sig(json_string, private_key)

# Assembling certificate
certificate = {
    'certificate_content': certificate_content,
    'signature': signature,
}


# ---------------------------- CLOSE SOCKET ------------------- #
client_socket.close()
