import hashlib
import pickle
import os
def EncryptionPassword(NameKey):
    users ={}
    with open('usrs_info.pickle','rb') as usrs_file:
        password = pickle.load(usrs_file)
        username = NameKey #The user name of login 
        userpasswd = password.get(NameKey) #The user password of login
        salt = os.urandom(32) #Prepare to change origin string password to 32-bit password
        key = hashlib.pbkdf2_hmac('sha256',userpasswd.encode('utf-8'),salt,100000)
        users[username] = {
            'salt' : salt,
            'key' : key
        }
    print(users[username]['salt'])


    