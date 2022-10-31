#Author: Fredrik Grahm-Haga

import hashlib

def registration():
    username = input("Please choose your username: ")
    password = input("Please choose a password (Your password should be at least 10 characters and should be a combination of digits, upper-case and lower-case letters, and special characters): ")
    while len(password) < 10:
        password = input("Your password is too short. Please choose a new password. (Your password should be at least 10 characters and should be a combination of digits, upper-case and lower-case letters, and special characters): ")
    
    sha1_login_salt = hashlib.sha1(bytes((username[:3] + password[:3]), encoding="utf-8")).digest() #Outputs hash of first 3 of username and password
    password_hashed_and_salted = hashlib.pbkdf2_hmac("sha256", password.encode(), sha1_login_salt, 10000) #Hashes with sha256 and sha1_login_salt as salt

    #Append to file shadow.txt
    file = open("misc/shadow.txt", "a")
    file.write(f"{username}${sha1_login_salt.hex()}${password_hashed_and_salted.hex()}\n") #Used .hex to get hex representations
    file.close()

    print("Congratulations! Your registration is completed! You must NOT share your password with others.")

registration()