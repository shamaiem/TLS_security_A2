import math
import random
from sympy import isprime
from sympy import primerange

#note: q and alpha are the same for both the client and server in the Diffie-hellman key exchange primitive

def FindPrimitiveRoot(q):
    for alpha in range(2,q):
        if all(pow(alpha,(q-1)//p,q)!=1 for p in primerange(2,q-1)):
            return alpha
    return None

def DHParameterGen(bits=8):
    #generating parameters for the Diffie Hellman key exchange i.e. q and alpha
    while True:
        q = random.randint(2**(bits-1), 2**bits-1)
        
        if (isprime(q)):
            alpha = FindPrimitiveRoot(q)
            if alpha is not None:
                return q,alpha

def DHCalculatePrivateKey(q):
    #generating a private integer key value that is less than X < q
    return random.randint(2,q-2)

def DHCalculatePublicKey(q,X):
    #Y= (alpha^X)mod q
    Y = (alpha**X)%q
    return Y

#Receives the others public key Y. Shared secret key K = ((Y)^own private key)mod q
def DHCalculateSharedKey(Y,X):
    K = ((Y**X)%q)
    return K

# ---- MAIN ----#
q,alpha = DHParameterGen()
print("Q = ", q,"Alpha = ", alpha)

# Calculations for A 
Xa=DHCalculatePrivateKey(q)
Ya=DHCalculatePublicKey(q,Xa)

print("A's public key is: ",{Xa})
print("A's private key is: ",{Ya})

# Calculations for B 
Xb=DHCalculatePrivateKey(q)
Yb=DHCalculatePublicKey(q,Xb)
print("B's public key is: ",{Xb})
print("B's private key is: ",{Yb})


# shared key caluclated by A 
shared_key_A = DHCalculateSharedKey(Yb,Xa)
print("A's shared key is: ",{shared_key_A})

# shared key caluclated by B
shared_key_B = DHCalculateSharedKey(Ya, Xb)
print("B's shared key is: ",{shared_key_B})

# The shared secrets should match
if shared_key_A == shared_key_B:
    print("Shared secrets match:", shared_key_A)
else:
    print("Shared secrets do not match")