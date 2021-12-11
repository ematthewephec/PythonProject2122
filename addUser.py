from pymongo import MongoClient


def __init__(self, **kwargs):
    self.create_database()  # call  our create database function




def create_database(self):
    # Creating a pymongo client
    client = MongoClient('localhost', 27017)

    # Getting the database instance
    db = client['mydb']
    print("Database created........")


def add_to_database(self):
    client = MongoClient('localhost', 27017)
    db = client['mydb']
    coll = db['example']
    doc1 = {"name": "Ram", "age": "26", "city": "Hyderabad"}
    coll.insert_one(doc1)


def get_data(self):
