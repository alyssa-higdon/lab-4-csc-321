from Crypto.Hash import SHA256
import hashlib
import random

def parta(input):
    hashed = hashlib.sha256(str(input).encode()).digest()
    print(hashed)
    return hashed

parta("hello panda")

def partb(input1, input2):
    parta(input1)
    parta(input2)

print("------------------")
partb("cat", "bat")
print("------------------")
partb("dog", "dog")
print("------------------")
partb("moon", "moom")

# can randomly generate input to put in the hash and compare the hash to each other in bits
def partc():
    m0 = random.getrandbits(16)
    m1 = random.getrandbits(16)
    

    m0_hashed = parta(m0)[:16] 
    m1_hashed = parta(m1)[:16]
    while(m0_hashed != m1_hashed):
        m1 = random.getrandbits(16)
        m1_hashed = parta(m1)[:16]
    
    print("m0: ")
    print(m0)
    print("m1: ")
    print(m1)
    print("m0_hashed: ")
    print(m0_hashed)
    print("m1_hashed: ")
    print(m1_hashed)
    print("success")
    return (m0, m1)

partc()