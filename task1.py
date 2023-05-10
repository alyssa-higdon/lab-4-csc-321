from Crypto.Hash import SHA256
import hashlib

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
partb("dog", "dof")
print("------------------")
partb("moon", "moom")

def partc():
    m0 = "bbbbbbbb"
    m1 = "bbbbbbbc"

    m0_hashed = parta(m0)[:16]
    m1_hashed = parta(m1)[:16]
    while(m0_hashed != m1_hashed):
        m1_bytes = b"".join([bytes(m1, "utf-8"), bytes(1)])
        m1 = str(m1_bytes)
        m1_hashed = parta(str(m1_bytes))[:16]
    
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