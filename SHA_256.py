import struct

# Define initial hash values (first 32 bits of the fractional parts of the square roots of the first 8 prime numbers)
h0 = 0x6a09e667
h1 = 0xbb67ae85
h2 = 0x3c6ef372
h3 = 0xa54ff53a
h4 = 0x510e527f
h5 = 0x9b05688c
h6 = 0x1f83d9ab
h7 = 0x5be0cd19

# Define constants (first 32 bits of the fractional parts of the cube roots of the first 64 prime numbers)
K = [
    0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5, 0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
    0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3, 0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
    0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc, 0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
    0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7, 0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
    0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13, 0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
    0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3, 0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
    0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5, 0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
    0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208, 0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2,
]

# Define functions
#function rotates right n bits
def rotr(x, n):
    return ((x >> n) | (x << (32 - n))) & 0xFFFFFFFF

#function shifts right n bits
def shr(x, n):
    return x >> n

def ch(x, y, z):
    return (x & y) ^ (~x & z)

def maj(x, y, z):
    return (x & y) ^ (x & z) ^ (y & z)

#function converts a string to a list of 32-bit words
def text_to_binary(text):
    binary_string = ""
    for char in text:
        # Convert each character to its ASCII code
        ascii_code = ord(char)

        # Convert the ASCII code to a binary string
        binary_representation = bin(ascii_code)[2:].zfill(8)

        # Append the binary representation to the result
        binary_string += binary_representation
    return binary_string


#-----preprocessing-----#
def preprocessing(data):
    # Append a single '1' bit to the data
    data += b'\x80'

    # Calculate the number of zero bytes to pad
    pad_length = 64 - (len(data) % 64)

    # Pad with zero bytes
    data += b'\x00' * pad_length

    # Append the length of the original message as a 64-bit big-endian integer
    length = len(data) * 8  # Calculate the message length in bits
    data += length.to_bytes(8, byteorder='big')

    return data

def split_data_into_chunks(data):
    chunk_size = 64  # 64 bytes (512 bits)
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    return chunks

def process_chunks(chunk,h0,h1,h2,h3,h4,h5,h6,h7):
    w = [0] * 64
    for i in range(16):
        w[i] = int.from_bytes(chunk[i * 4:i * 4 + 4], byteorder='big')

    for i in range(16, 64):
        sigma0 = rotr(w[i - 15], 7) ^ rotr(w[i - 15], 18) ^ shr(w[i - 15] , 3)
        sigma1 = rotr(w[i - 2], 17) ^ rotr(w[i - 2], 19) ^ shr(w[i - 2],10)
        w[i] = (w[i - 16] + sigma0 + w[i - 7] + sigma1) & 0xFFFFFFFF

    a = h0
    b = h1
    c = h2
    d = h3
    e = h4
    f = h5
    g = h6
    h = h7

    for i in range(64):
        S1 = rotr(e, 6) ^ rotr(e, 11) ^ rotr(e, 25)
        c = ch(e,f,g)
        temp1 = h + S1 + c + K[i] + w[i]
        S0 = rotr(a, 2) ^ rotr(a, 13) ^ rotr(a, 22)
        m= maj(a,b,c)
        temp2 = S0 + m

        h = g
        g = f
        f = e
        e = (d + temp1) & 0xFFFFFFFF
        d = c
        c = b
        b = a
        a = (temp1 + temp2) & 0xFFFFFFFF
    
    h0 = (h0 + a) & 0xFFFFFFFF
    h1 = (h1 + b) & 0xFFFFFFFF
    h2 = (h2 + c) & 0xFFFFFFFF
    h3 = (h3 + d) & 0xFFFFFFFF
    h4 = (h4 + e) & 0xFFFFFFFF
    h5 = (h5 + f) & 0xFFFFFFFF
    h6 = (h6 + g) & 0xFFFFFFFF
    h7 = (h7 + h) & 0xFFFFFFFF

    return h0, h1, h2, h3, h4, h5, h6, h7

def sha256(data):
    data = preprocessing(data)
    chunks = split_data_into_chunks(data)

    # Initial hash values
    h0 = 0x6a09e667
    h1 = 0xbb67ae85
    h2 = 0x3c6ef372
    h3 = 0xa54ff53a
    h4 = 0x510e527f
    h5 = 0x9b05688c
    h6 = 0x1f83d9ab
    h7 = 0x5be0cd19

    # Process each chunk
    for chunk in chunks:
        h0, h1, h2, h3, h4, h5, h6, h7 = process_chunks(chunk, h0, h1, h2, h3, h4, h5, h6, h7)

    # Concatenate the final hash values
    final_hash = struct.pack('>IIIIIIII', h0, h1, h2, h3, h4, h5, h6, h7)

    return final_hash

