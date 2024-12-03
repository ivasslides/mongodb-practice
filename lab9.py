#!/home/codespace/.python/current/bin/python3
from pymongo import MongoClient, errors
from bson.json_util import dumps

# connecting to mongodb
MONGOPASS = 'R6O0pEawYZzgbKNg'
uri = "mongodb+srv://ilianavass:R6O0pEawYZzgbKNg@cluster0.nowii.mongodb.net/fbv2sc?retryWrites=true&w=majority"
client = MongoClient(uri)

# going to database and creating collection
thisdb = client["fbv2sc"]
yacht_clubs = thisdb["yacht_clubs"]

# docs to add
docs = [
    {"name": "Toms River Yacht Club", "colors": "blue & white", "location": "the Toms River"},
    {"name": "Metedeconk River Yacht Club", "colors": "blue & white", "location": "the Metedeconk River"},
    {"name": "Pine Beach Yacht Club", "colors": "green & white", "location": "the Toms River"},
    {"name": "Ocean Gate Yacht Club", "colors": "red, white & blue", "location": "the Toms River"},
    {"name": "Mantoloking Yacht Club", "colors": "red & white", "location": "the Metedeconk River"}
]

# inserting docs to collection
yacht_clubs.insert_many(docs)

# query to display only docs w location = the Toms River
get_record = yacht_clubs.find({"location": "the Toms River"})
print(dumps(get_record, indent=2))
