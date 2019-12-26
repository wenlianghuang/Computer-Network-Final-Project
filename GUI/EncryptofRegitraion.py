import hashlib
import pickle
import os

def EncryptionKey():
    import base64
    from cryptography.hazmat.backends import default_backend
    from cryptography.hazmat.primitives import hashes
    from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
    
    password_provide = password.get(NameKey)
    password_key = password_provide.encode()
    salts = os.urandom(16)
    kdf = PBKDF2HMAC (
            algorithm=hashes.SHA256,
            length=32,
            salt=salt,
            iteration=100000,
            backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_key))
    return key


def EncryptionPassword(userpasswd):
    from cryptography.fernet import Fernet
    with open('./user_key.pickle','rb') as usrs_file:
        key = pickle.load(usrs_file)
        print(key)
        f = Fernet(key)
        encrypted = f.encrypt(userpasswd.encode('utf-8'))

        return encrypted

        #hashupd = hashlib.sha256()
        #hashupd.update(userpasswd.encode('utf-8'))
        #userpasswd = hashupd.hexdigest()
        #print(userpasswd)

        
        ##20191221
        #salt = os.urandom(32) #Prepare to change origin string password to 32-bit password
        #key = hashlib.pbkdf2_hmac('sha256',userpasswd.encode('utf-8'),salt,100000)
        #users[username] = {
        #    'salt' : salt,
        #    'key' : key
        #}
    #print(users[username]['key'])


    
