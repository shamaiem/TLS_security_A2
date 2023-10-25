import ast
import base64
import cryptography.fernet
from cryptography.fernet import Fernet
import random
import math
import SHA256_module
import json
import hashlib
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



def RSAencryptI(plaintext, public_key):
    e, n = public_key

    if plaintext >= n:
        print("plainText= ",plaintext)
        print("n=",n)
        raise ValueError("Plaintext must be less than n for encryption.")
    ciphertext = pow(plaintext, e, n)
    return ciphertext

def RSAdecryptI(ciphertext, private_key):

    d, n = private_key
    if ciphertext >= n:
        raise ValueError("Ciphertext must be less than n for decryption.")
    plaintext = pow(ciphertext, d, n)
    return plaintext
