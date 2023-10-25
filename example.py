<<<<<<< Updated upstream
# Step 1: Generate a key pair (usually done beforehand)
import encryption_module
import json
import RSAencryption_module
import SHA256_module

private_key, public_key =encryption_module.RSAkeygeneration(8)
=======
<<<<<<< HEAD
# pip install cryptography
import ast
import base64
import cryptography.fernet
from cryptography.fernet import Fernet
import random
import math
import SHA_256
import json
import hashlib

#---------------------------------------------------AES cryptography---------------------------------------------------#
# Generate a random AES key
AESkey = cryptography.fernet.Fernet.generate_key()
=======
# Step 1: Generate a key pair (usually done beforehand)
import encryption_module
import json
import RSAencryption_module
import SHA256_module
>>>>>>> Stashed changes

private_key, public_key =encryption_module.RSAkeygeneration(8)
>>>>>>> 9646003638707f773e9836277b23191b424179b4


<<<<<<< HEAD
def convert_to_fernet_key(input_key):
    # Hash the input key using a cryptographic hash function (SHA-256)
    hashed_key = hashlib.sha256(input_key).digest()

    # Truncate the hashed key to 32 bytes (256 bits) to match Fernet key size
    truncated_key = hashed_key[:32]
=======
# Step 3: Certificate signing
certificate_hash=SHA256_module.sha256(str(certificate_content).encode())
certificate_hash_str=str(certificate_hash)

json_string = json.dumps(certificate_content)
signature = encryption_module.create_sig(json_string, private_key)
<<<<<<< Updated upstream
=======
>>>>>>> 9646003638707f773e9836277b23191b424179b4
>>>>>>> Stashed changes

    # Convert the truncated key to base64-encoded bytes
    fernet_key = Fernet(base64.urlsafe_b64encode(truncated_key))

    return fernet_key

<<<<<<< Updated upstream
=======
<<<<<<< HEAD
# Encrypt a message
def AESencrypt(plain_text, key):
    cipher = cryptography.fernet.Fernet(key)
    encrypted_message = cipher.encrypt(plain_text.encode())
    return encrypted_message
=======
>>>>>>> Stashed changes
valid=encryption_module.verify_sig(json_string,signature,public_key)
print("with hashing as string: ",valid)
>>>>>>> 9646003638707f773e9836277b23191b424179b4

# Decrypt a message
def AESdecrypt(cipher_text, key):
    cipher = cryptography.fernet.Fernet(key)
    decrypted_message = cipher.decrypt(cipher_text)
    return decrypted_message.decode()

<<<<<<< Updated upstream
sig2=RSAencryption_module.create_sig('alice',private_key)
print("with hashing as int the message: ",RSAencryption_module.verify_sig('alice',sig2,public_key))

=======
<<<<<<< HEAD

#---------------------------------------------------RSA cryptography---------------------------------------------------#

def RSAkeygeneration (bits):
    # Choose two large prime numbers
    p = generate_prime(bits)
    q = generate_prime(bits)
    
    # Calculate n (modulus)
    n = p * q
    
    # Calculate phi (Euler's totient function)
    phi = (p - 1) * (q - 1)

    # print(f'p = {p}, q = {q}, n = {n} and phi = {phi}')

    # Choose an integer e such that 1 < e < phi and gcd(e, phi) = 1
    e = choose_e(phi)
    
    # Calculate the  d (modular inverse of e mod phi)
    d = mod_inverse(e, phi)

    public_key = (e, n)
    private_key = (d, n)
  
    return public_key, private_key

#randomly generating numbers and then checking if they are prime
def generate_prime(bits):
    while (1):
        number = random.getrandbits(bits)
        if check_prime(number):
            return number

def check_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    if n == 2:
        return True

    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

#chosing the value of 'e' such that it is relatively prime with phi
def choose_e(phi):
    e = random.randint(2, phi - 1)      #generating a random value
    
    while math.gcd(e, phi) != 1:        #checking if the value is relatively prime with phi in loop till gcd =1
        e = random.randint(2, phi - 1)
    return e

#calculating the modular inverse of e mod phi
def mod_inverse(e, phi):
    i = 1
    while True:
        d = (phi * i + 1) // e
        if (d * e) % phi == 1:
            return d
        i += 1
  
    return None


def RSAencryptCH(plaintext, public_key):
    e, n = public_key
    #json_dict = json.loads(plaintext)
    # Serialize the dictionary back into a JSON string (this step is optional)
    serialized_json = json.dumps(plaintext)
    encrypted_text = [pow(ord(char), e, n) for char in serialized_json]
    
    return encrypted_text

def RSAdecryptCH(encrypted_text, private_key):
    d, n = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in encrypted_text]
    # Convert the list of characters to a single string
    decrypted_string = ''.join(decrypted_text)
    # Replace any non-printable or non-ASCII characters
    decrypted_string = ''.join(char for char in decrypted_string if char.isprintable() or char.isascii())
    return decrypted_string


def create_sig(message, private_key):
    signature = RSAencryptCH(message, private_key)
    return signature


def verify_sig(message, signature, public_key):
    decrypted_message_digest = RSAdecryptCH(signature, public_key)
    decrypted_message_digest = json.loads(decrypted_message_digest)
    # print("decrypted_message_digest: ",(decrypted_message_digest))
    # print("message: ",(message))
    if ((decrypted_message_digest ))==(message):
        return True  # Signature is valid
    else:
        return False  # Signature is invalid
    
def convert_to_tuple(key):
    resulting_tuple = ast.literal_eval(key)       #returns a list from the string
    Key_tuple=tuple(resulting_tuple)
    return Key_tuple

#---------------------Int encryption and decryption---------------------#

# def RSAencryptI(plaintext, public_key):
#     e, n = public_key
#     if plaintext >= n:
#         print("plainText= ",plaintext)
#         print("n=",n)
#         raise ValueError("Plaintext must be less than n for encryption.")
#     ciphertext = pow(plaintext, e, n)
#     return ciphertext

# def RSAdecryptI(ciphertext, private_key):
#     d, n = private_key
#     if ciphertext >= n:
#         raise ValueError("Ciphertext must be less than n for decryption.")
#     plaintext = pow(ciphertext, d, n)
#     return plaintext
=======
sig2=RSAencryption_module.create_sig('alice',private_key)
print("with hashing as int the message: ",RSAencryption_module.verify_sig('alice',sig2,public_key))

>>>>>>> Stashed changes
print(public_key)
encrypted=encryption_module.RSAencryptCH(json.dumps(public_key),private_key)
decrypted=encryption_module.RSAdecryptCH(encrypted,public_key)
print(encryption_module.convert_to_tuple(decrypted) == public_key)
<<<<<<< Updated upstream
=======
>>>>>>> 9646003638707f773e9836277b23191b424179b4
>>>>>>> Stashed changes
