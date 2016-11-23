from flask import Flask, jsonify
from pymongo import MongoClient

# Using Flask framework to manage API

# Create a Flask instance
app = Flask(__name__)

# IP adress of the VM where MongoDB is. (VM 'UXE' using Red Hat)
ip_address = "138.195.53.231"
# Connect to MongoDB server running on 27017
client = MongoClient("mongodb://%s:27017" %ip_address)
db = client.db_tpnosql

# Return list of all available languages
# /languages.json
@app.route('/languages.json', methods=['GET'])
def return_languages():
    # MongoDB request
    result = db.repository.distinct("language")
    # Convert the result to JSON and return
    return jsonify(result)

if __name__ == "__main__":
    app.run()
