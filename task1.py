from Crypto.Hash import SHA256
import hashlib
import random
import time

def parta(input):
    hashed = hashlib.sha256(str(input).encode()).hexdigest()
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
def partc(digest):
    # hashes are key and values are message
    hashes = {}
    m0 = random.getrandbits(256)
    m0_hashed = parta(m0)[:digest] 
    inputs = 1
    start = time.time()
    while(m0_hashed not in hashes.keys() and (m0 in hashes.values())):
        hashes[m0_hashed] = m0
        m0 = random.getrandbits(256)
        m0_hashed = parta(m0)[:digest]
        inputs += 1
    end = time.time()
    print("digest: ", digest)
    print("m0: ", m0)
    # print("m1: ", m1)
    print("m0_hashed: ", m0_hashed)
    # print("m1_hashed: ", m1_hashed)
    print("success")
    print("total amoung of inputs: ", inputs)
    print("total time: ", end - start)
    # return (m0, m1)
    return m0

n = 2
while(n < 51):
    partc(n)
    n += 2