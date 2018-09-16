'''
Functions for CRUD operations on the database
'''

from pymongo import MongoClient
from JSONEncoder import *
import json

client = MongoClient('localhost', 27017)
db = client['information-display']
jsonEncoder = JSONEncoder()

def addEntry(collectionName, newEntry):
    collection = db[collectionName]
    collection.insert_one(json.loads(newEntry))

def updateEntry(collectionName, newEntry):
    collection = db[collectionName]
    lastEntryId = collection.find_one()['_id']
    if lastEntryId is not None:
        collection.find_one_and_replace(
            {'_id': lastEntryId},
            json.loads(newEntry)
        )
    else:
        addEntry(collectionName, newEntry)
        
def getEntry(collectionName):
    collection = db[collectionName]
    return JSONEncoder().encode(collection.find_one())