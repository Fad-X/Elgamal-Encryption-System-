import time
import random 
from math import pow

def decrypt(en_msg, p, key, q): 
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
         dr_msg.append(chr(int(en_msg[i]/h)))
    return dr_msg
 

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
 
def power(a, b, c):
    x = 1
    y = a
    while b > 0:
        if b % 2 != 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2) 

    return x % c
    
    

en_msg=[]
length = int(input("What is the LENGTH OF Ciphertext? "))
for i in range(0,length):
	values = int(input(f'Enter value{i + 1}: '))
	en_msg.append(values)
	
p = int(input("Enter the Cipher Value: "))
q = int(input("Enter the Value for The Prime Number: "))
key = int(input("Enter Sender's KEY value: "))
dr_msg = decrypt(en_msg, p, key, q)


dmsg = ''.join(dr_msg)

time.sleep(3)
print("\n \n \n The Plaintect is ", dmsg);
 
