import random
import math
from sympy import isprime

def generate_prime_number(bits=8):
    while True:
        primeNum = random.getrandbits(8)
        if primeNum % 2 == 0: #even numbers greater than 2 cannot be prime
            primeNum +=1
        if isprime(primeNum):
            return primeNum

def multiplicative_inverse(e,phi):
    d = 0 
    x1, x2 = 0 , 1
    y1, y2 = 1 , 0

    while phi != 0:
        q = e // phi

        
gcd_result = math.gcd(a,b)

