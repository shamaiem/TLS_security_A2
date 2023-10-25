def multiplicative_inverse(e, phi):
    d = 0
    x1, x2 = 0, 1
    y1, y2 = 1, 0
    while phi != 0:
        q = e // phi
        e, phi = phi, e % phi
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
    d = x1
    return d

def generate_keypair(bits):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Commonly used public exponent
    d = multiplicative_inverse(e, phi)
    return (n, e), (n, d)

def encrypt(public_key, plaintext):
    n, e = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    n, d = private_key
    decrypted_text = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(decrypted_text)

if __name__ == "__main__":
    bits = 128  # Adjust the bit length as needed
    public_key, private_key = generate_keypair(bits)

    message = "Hello, RSA encryption!"
    print("Original message:", message)

    encrypted_message = encrypt(public_key, message)
    print("Encrypted message:", encrypted_message)

    decrypted_message = decrypt(private_key, encrypted_message)
    print("Decrypted message:", decrypted_message)
