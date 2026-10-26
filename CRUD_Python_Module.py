# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username 
        PASS = password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
        # was not apart of the assignment
        
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            self.database.animals.insert_one(data)  # data should be dictionary  
            return True # returns true or false depending if the data is empty or not.
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 
            return False

    # Create method to implement the R in CRUD.
    
    def read(self, data):
        if data is not None:
            result = self.database.animals.find(data) # similarily to the create method, returns the list of the find. Doesn't return true or false.
            return list(result)
        else:
            raise Exception("Nothing to save, because data parameter is empty") # returns the list if successful
            
    def update(self, query, update):
        if not query:
            raise Exception("Query not available") # will fail if query has no value
        elif not update:
            raise Exception("No updatable value") # similarily to query, will fail if there is no value
        else:
            updateValid = self.database.animals.update_many(query, {"$set": update}) # then update_many the query with update
            
            return updateValid.modified_count if updateValid.modified_count > 0 else 0 # returns the modified count if changed, otherwise returns 0
        
    def delete(self, query):
        if not query:
            raise Exception("Query not available") # works similarily
        else:
            deleteValid = self.database.animals.delete_many(query) #dletes the query'd amount
            
            return deleteValid.deleted_count if deleteValid.deleted_count > 0 else 0 # works similarily