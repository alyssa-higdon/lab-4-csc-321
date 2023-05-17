import nltk
nltk.download()
from nltk.corpus import words
words.words()



# Given: salt, hashed, hashing algorithm
# Do:
# Go through each world in corpus and hash it with salt and see if the resulting
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
    while(j < 22):
        salt += line[i + j]
        j +=1
    hash = line[i + j:]
    
    print(user)
    print(algorithm)
    print(workfactor)
    print(salt)
    print(hash)


    print(nltk.corpus.abc.words())

bCrypt("Bilbo:$2b$08$L.z8uq99JkFAvX/Q1jGRI.TzrHIIxWMoRi/VzO1sj/UvVFPgW8dW.")
    
