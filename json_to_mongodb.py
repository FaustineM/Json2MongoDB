import json
import pprint
from pymongo import MongoClient
from flask import Flask

# TP NoSQL
# Extract data from Github API into MongoDB

# JSON file containing data on repositories from Github :
repos_json = json.load(open("repos_data.json"))

# IP adress of the VM where MongoDB is. (VM 'UXE' using Red Hat)
ip_address = "138.195.53.231"
# Connect to MongoDB server running on 27017
client = MongoClient("mongodb://%s:27017" %ip_address)
db = client.db_tpnosql

# Extract repositories' name and id, owners' name and languages
# from json file to MongoDB
for item in repos_json :
    repos_dict = {}
    repos_dict['id']=item.get('id')
    repos_dict['name']=item.get('name')
    repos_dict['owner']=item.get('owner').get('login')
    repos_dict['language']=item.get('language')
    # Using replace_one instead of insert in order to avoid copying all the data each time the script is launched.
    # If a record with this id already exist, replace it, if not create it (True)
    db.repository.replace_one({'id': item.get('id')}, repos_dict, True)
