import time
import random 
from math import pow
 
a = random.randint(2, 10)
 
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
       return gcd(b, a % b)
 
# Generating large random numbers
def gen_key(q):
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
    return key
 

       
              
                     
def encrypt(msg, q, h, g):
    en_msg = []
    k = gen_key(q)# Private key for sender
    s = power(h, k, q)
    p = power(g, k, q)
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
    return en_msg, p
 
                                                         
                                          
def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2) 

    return x % c
 
msg = input("Enter the correct Plaintext: ")
print("Original Message :", msg)
q = int(input("Enter value for Large Prime Number: "))
g = int(input("Enter Public Key Value: "))
h = int(input("Enter Sender's Private Key: "))


en_msg, p = encrypt(msg, q, h, g)
time.sleep(2)
print("-------------------")
print("\n \n \n Cipher Text is",en_msg)
print("The length of the Cipher Text is",len(en_msg))
print("-------------------")
print("\n Our Cipher Value is",p)
print("-------------------")
