import json
import pprint
from pymongo import MongoClient

# JSON file
repos = json.load(open("repos_data.json"))

# IP adress of the VM where MongoDB is.
ip_address = "0.0.0.0"

# Connect to the mongoDB
client = MongoClient("mongodb://%s:27017" %ip_address)
db = client.db_tpnosql

print(client)

# Extract repositories' name and id, owners' name and languages from json file to MongoDB
for item in repos :
    repos_dict = {}
    repos_dict['id']=item.get('id')
    repos_dict['name']=item.get('name')
    repos_dict['owner']=item.get('owner').get('login')
    repos_dict['language']=item.get('language')
    # Using replace_one instead of insert in order to avoid copying all the data each time the script is launched.
    # If a record with this id already exist, replace it, if not create it (True)
    db.repository.replace_one({'id': item.get('id')}, repos_dict, True)
