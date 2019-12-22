import pymongo
import pickle
import hashlib
#Connect to the remote dongodb 
def LoadinDBFunction(username,userpassword):
    hashupd = hashlib.sha256()
    hashupd.update(userpassword.encode('utf-8'))
    userpassword = hashupd.hexdigest()
    print(userpassword)
    myclient = pymongo.MongoClient("mongodb+srv://WenLiangMatt:wenliang75@cluster0-ejyss.mongodb.net/test&authMechanism=SCRAM-SHA-256")
    print(myclient.list_database_names())

    #Get table from db
    mydb = myclient.MattDB
    print(mydb.list_collection_names())
    print(mydb['WenLiang']['username'])
    mycol = mydb['WenLiang']
    mydict = {'username':username,'userpassword':userpassword}
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

