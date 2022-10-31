# Just in case I need my name here: Fredrik Grahm-haga

import string
import math

alphabet = list(string.ascii_lowercase)

def keyGen(msg, key):
    keyMod = key
    while len(msg) > len(keyMod):
        keyMod += key
    return keyMod

def vignere(mode, msg, key):
    keyMod = keyGen(msg, key)
    msgMod = ""
    keyI = 0
    if mode == "encode":
        modeNum = 1
    elif mode == "decode":
        modeNum = -1
    else:
        return "Use encode/decode"

    for i in range(len(msg)):
        if msg[i] in alphabet:
            cipherIndex = alphabet.index(msg[i]) + ((alphabet.index(keyMod[keyI]) * modeNum))
            cipherIndex -= (cipherIndex // (len(alphabet)) * len(alphabet))
            msgMod += alphabet[cipherIndex]
            keyI += 1
        else: msgMod += msg[i]
    return msgMod

def transpositionEncode(msg, key):
    msgChunks = []
    keyLen = len(key)
    chunkCount = (math.ceil(len(msg)/keyLen))
    msg += " " * ((chunkCount * keyLen) - len(msg)) #Pad Msg
    for i in range(chunkCount): #Chunk
        msgChunks.append(msg[i*keyLen:keyLen + (i*keyLen)])

    msgModList = []
    for i in range(len(msgChunks)): #Generate Empty Chunked List
        msgModList.append(list("_" * keyLen))
        
    for i in range(len(msgChunks)): #Move columns
        for j in range(keyLen):
            msgModList[i][int(key[j]) - 1] = msgChunks[i][j]

    msgMod = ""
    for i in range(keyLen): #List Columns
        for chunk in msgModList:
            msgMod += chunk[i]
    return msgMod

def transpositionDecode(msg, key):
    msgChunks = []
    keyLen = len(key)
    rowLen = (len(msg)//keyLen)
    for i in range(len(msg) // rowLen): #Chunk
        msgChunks.append(msg[i*rowLen:rowLen + (i*rowLen)])

    msgModList = []
    for i in range(len(msgChunks)): #Generate Empty Chunked List
        msgModList.append([])

    for i in range(keyLen): #Move columns
        keyI = int(key[i])-1
        msgModList[i] = msgChunks[keyI]

    msgMod = ""
    for i in range(rowLen): #List Columns
        for j in range(len(msgModList)):
            msgMod += msgModList[j][i]
    
    return msgMod

def encode(msg, k1, k2):
    print("\nOriginal message: " + msg)
    txt1 = vignere("encode", msg, k1)
    print("\nEncryption step 1: " + txt1)
    txt2 = transpositionEncode(txt1, k2)
    print("\nEncryption step 2: " + txt2)
    txt3 = vignere("encode", txt2, k1)
    print("\nEncryption step 3: " + txt3)
    txt4 = transpositionEncode(txt3, k2)
    return ("\nFinal encryption step: " + txt4)

def decode(cipherMsg, k1, k2):
    print("\nOriginal cipher message: " + cipherMsg)
    txt1 = transpositionDecode(cipherMsg, k2)
    print("\nDecryption step 1: " + txt1)
    txt2 = vignere("decode", txt1, k1)
    print("\nDecryption step 2: " + txt2)
    txt3 = transpositionDecode(txt2, k2)
    print("\nDecryption step 3: " + txt3)
    txt4 = vignere("decode", txt3, k1)
    return ("\nFinal decryption step: " + txt4)

print(encode("Cyber security is technologically complicated. It is a process not a product.", "cryptographyisfun", "34157268"))
print(decode("w cs aln bwyvlemhf.eu hu wv tairkiokr iyjl dwf  kIfrmajlwjhbdqCl ety wl.razx gj ", "cryptographyisfun", "34157268"))

print(vignere("decode", "tsaatmvttlezlwbhvbproaszletpdmaliaxplvmhvmvrtfxevhqmjmyivaxgwiavjkvqxhrqlwquxplawyplalwziboeboedlfmlrjyiijlmkevkovvaqaevkxpvwmalialicijlivivmhgplhiuhlvrwaovvaqa.", "hei"))