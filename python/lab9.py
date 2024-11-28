#!/home/codespace/.python/current/bin/python3
from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *

MONGOPASS = os.getenv('MONGOPASS')
uri = "mongodb+srv://cluster0.m3fek.mongodb.net/fbv2sc"
client = MongoClient(rui, username='ds2022', password=MONGOPASS)

thisdb = client.fbv2sc
clubs = thisdb.clubs


docs = {
   {"name": "Toms River Yacht Club", "colors": "blue & white", "location": "the Toms River"},
   {"name": "Metedeconk River Yacht Club", "colors": "blue & white", "location": "the Metedeconk River"}, 
   {"name": "Pine Beach Yacht Club", "colors": "green & white", "location": "the Toms River"}, 
   {"name": "Ocean Gate Yacht Club", "colors": "red, white & blue", "location": "the Toms River"},
   {"name": "Mantoloking Yacht Club", "colors": "red & white", "location": "the Metedeconk River"}
}

clubs.insert_many(docs)
get_record = clubs.find({"location":"the Toms River"})
print(dumps(get_record, indent=2))
