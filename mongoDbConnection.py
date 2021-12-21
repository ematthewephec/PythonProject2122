from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://dbUser:lolo123@cluster0.6pkp4.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["test"]
collection = db["test"]


def edit_data(filter, update):
    collection.update_one(filter, {"$set": update})
    print("Modification effectué")

def delete_data(delete_item):
    collection.delete_one(delete_item)
    print("Suppression effectué")

def insert_data(item):
    collection.insert_one(item)

def fin_data(search):
    doc = collection.find(search)
    return doc

if __name__ == "__main__":
    try:
        toto = {"_id":4, "lastname":"Moulart", "firstname":"Sam", "tag":["2T", "1T"]}
        insert_data(toto)

    except:
        print("Erreur")