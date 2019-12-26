import pymongo
import pickle
import hashlib
from EncryptofRegitraion import EncryptionPassword
#Connect to the remote dongodb 
def LoadinDBFunction(username,userpassword):
    #Encrypted password
    encryptedpw = EncryptionPassword(userpassword)
    
    #myclient = pymongo.MongoClient("mongodb+srv://WenLiangMatt:wenliang75@cluster0-ejyss.mongodb.net/test&authMechanism=SCRAM-SHA-256")
    myclient = pymongo.MongoClient("mongodb+srv://WenLiangMatt:wenliang75@cluster0-ejyss.mongodb.net/test")
    print(myclient.list_database_names())

    #Get table from db
    mydb = myclient.MattDB
    print(mydb.list_collection_names())
    mycol = mydb['WenLiang']
    #mydict = {'username':username,'userpassword':userpassword}
    mydict = {'username':username,'userpassword':encryptedpw}
    mycol.insert_one(mydict)
    
    #with open('./usrs_info.pickle','rb') as usr_file:        
    #    tot_name = pickle.load(usr_file)
    #    i = 1
    #    for key in tot_name:
    #        print(key)
    #        print(tot_name[key])
    #        mydict = { '_id':i, 'username':key,'userpassword':tot_name[key]}
    #        mycol.insert_one(mydict)
    #        i+=1

