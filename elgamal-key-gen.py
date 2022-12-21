import random 
from math import pow


def power(a, b, c):

    x = 1

    y = a
 

    while b > 0:

        if b % 2 != 0:

            x = (x * y) % c;

        y = (y * y) % c

        b = int(b / 2)
 

    return x % c


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
       return gcd(b, a % b)

def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key


q = random.randint(pow(10, 20), pow(10, 50))
g = random.randint(2, q)
key = gen_key(q)
h = power(g, key, q)

print("The Public key  is",g)
print("-------------------")
print("The large Prime Number used is ",q)
print("-------------------")
print("The Sender's private Key used in Encryption is",h)
print("-------------------")
print("Our Receiver's Private KEY for decryption is ",key)
print("-------------------")


