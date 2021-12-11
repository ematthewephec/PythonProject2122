from pymongo import MongoClient

#Connect to DB
client = MongoClient(port=12345)
db=client.noyau

#Get Data from command line
