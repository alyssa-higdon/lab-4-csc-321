import nltk
nltk.download()
from nltk.corpus import words
words.words()
import bcrypt
import time
import base64
# Given: salt, hashed, hashing algorithm
# Do: go through each world in corpus and hash it with salt and see if the resulting
# hash matches the given hashed
def bCrypt(line):
    user = ""
    algorithm = "2b"
    workfactor = ""
    salt = ""
    hash = ""
    i = 0
    while(line[i] != ":" and line[i + 1] != "$"):
        user += line[i]
        i += 1
    i += 5 #offset to workfactor
    while(line[i] != "$"):
        workfactor += line[i]
        i +=1
    i +=1
    j = 0
    salt += "$" + algorithm + "$" + workfactor
    while(j < 22):
        salt += line[i + j]
        j +=1
    hash = line[i + j:]
    print(user)
    print(algorithm)
    print(workfactor)
    print(salt)
    print(hash)
    start = time.time()
    for word in nltk.corpus.abc.words():
        if len(word) >= 6 and len(word) <= 10:
            print("type of salt before .encode: ", type(salt))
            print("type of salt: ", type(salt.encode('ascii')))
            print("type of word converted: ", type(word.encode('utf8')))
            # if bcrypt.hashpw(word.encode('ascii'), salt.encode('utf8')) == hash:
            # if bcrypt.hashpw(word.encode('ascii'), base64.b64decode(salt).encode('utf8')) == hash:
            salt2 = salt.encode()
            salt3 = base64.b64decode(salt2)
            print("type of salt3: ", type(salt3))
            if bcrypt.hashpw(word.encode('ascii'), salt3) == hash:
                end = time.time()
                print("nltk word: ", word)
                print("hash: ", hash)
                print("Start: ", start)
                print("End: ", end)
                print("Total Time: ", end - start)
                return True
    print("Returned False")
    print("hash: ", hash)
    print("Start: ", start)
    print("End: ", end)
    print("Total Time Elapsed: ", end - start)
    return False
    
#  Given: salt, hashed, hashing algorithm
# Do: go through each world in corpus and hash it with salt and see if the resulting hash matches the given hashed 
    print(nltk.corpus.abc.words())

bCrypt("Bilbo:$2b$08$L.z8uq99JkFAvX/Q1jGRI.TzrHIIxWMoRi/VzO1sj/UvVFPgW8dW.")
    
