#Author: Fredrik Grahm-Haga

import hashlib

def authentication():
    username = input("Please input your username: ")
    password = input("Please input your password: ")

    #Get file as 2d array
    shadow_array = []
    with open("misc/shadow.txt") as f:
        for line in f.readlines():
            shadow_array.append(line.rstrip("\n").split("$"))
    
    #Loop through all entries in shadow.txt
    for entry in shadow_array:
            if username == entry[0]: #If username found in shadow.txt
                password_hashed_and_salted = hashlib.pbkdf2_hmac("sha256", password.encode(), bytes.fromhex(entry[1]), 10000).hex() #Hashes with sha256 and sha1_login_salt as salt
                if password_hashed_and_salted == entry[2]: #If stored and newly calculated hashed/salted passwords are identical
                    print("You’re successfully logged in")
                    return
    
    print("The provided username and password do not match. Please try again.")

authentication()