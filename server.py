import socket
import encryption_module
import json
import RSAencryption_module

client_message = " "

# -------------------- FUNCTIONS ------------------ #

# Function to take input from server
def server_response_input():
    print("--------------------------")
    print("Enter server's response: ")
    print("--------------------------")
    response = input()
    return response

# Function that receives clients message
def recv_client_message():
    print("---------------------------------")
    print(f"Received from client: {client_message}")
    print("--------------------------------")
    return client_message

def establish_server_handshake():
    # Conduct a 3-way handshake and accept the connection 
    client_message = client_socket.recv(1024).decode()
    print(f"Receieved message {client_message} from {client_address},")
    if client_message == "Client Hello!":
        server_response = "Server Hello!"
        client_socket.send(server_response.encode())
        print(f"Sent response {server_response} to {client_address}")
    else:
        print("No hello message from client!")
    return

# ------------------- FUNCTIONS END ------------- #

# Server Settings
HOST = 'localhost'
PORT = 12345

# Creating a Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server is listening on {HOST}:{PORT}")
# Accept a client connection
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

establish_server_handshake()

# ----------------------- ENCRYPTED COMMUNICATION ----------------- 
private_key, public_key =encryption_module.RSAkeygeneration(8)
print(f"Server Public key {public_key}, Server Private Key {private_key}")

# Initializing certificate content
certificate_content = {
    'subject': 'server',
    'public_key': public_key
}

# Signing certificate
json_string = json.dumps(certificate_content)
signature = encryption_module.create_sig(json_string, private_key)

# Assembling certificate
certificate = {
    'certificate_content': certificate_content,
    'signature': signature,
}

# Verifying certificate
valid=encryption_module.verify_sig(json_string,signature,public_key)
print("with hashing as string: ",valid)

print("")

sig2=RSAencryption_module.create_sig('server',private_key)
print("with hashing as int the message: ",RSAencryption_module.verify_sig('server',sig2,public_key))

print(public_key)
encrypted=encryption_module.RSAencryptCH(json.dumps(public_key),private_key)
decrypted=encryption_module.RSAdecryptCH(encrypted,public_key)
print(encryption_module.convert_to_tuple(decrypted) == public_key)

# while True:
#     client_message = recv_client_message()
#     if not client_message:
#         break
#     response = server_response_input()
#     client_socket.send(response.encode())


# ---------------------------- CLOSE SOCKET ------------------- #
client_socket.close()
