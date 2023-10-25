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


def convert_to_fernet_key(input_key):
    # Hash the input key using a cryptographic hash function (SHA-256)
    hashed_key = hashlib.sha256(input_key).digest()

    # Truncate the hashed key to 32 bytes (256 bits) to match Fernet key size
    truncated_key = hashed_key[:32]

    # Convert the truncated key to base64-encoded bytes
    fernet_key = Fernet(base64.urlsafe_b64encode(truncated_key))

    return fernet_key

# Encrypt a message
def AESencrypt(plain_text, key):
    cipher = cryptography.fernet.Fernet(key)
    encrypted_message = cipher.encrypt(plain_text.encode())
    return encrypted_message

# Decrypt a message
def AESdecrypt(cipher_text, key):
    cipher = cryptography.fernet.Fernet(key)
    decrypted_message = cipher.decrypt(cipher_text)
    return decrypted_message.decode()

