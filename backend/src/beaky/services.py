import requests
import json
import csv
import json
import os
import sys
import datetime
import time
from pymongo import MongoClient

def signUp(username, password, email, labels):
    client = MongoClient('mongo_db', 27017)
    db = client["ScicatDB"]
    db.authenticate('mongoApp', 'mongoAppPass')

    newUser = dict()
    newUser["username"] = username
    newUser["password"] = password
    newUser["email"] = email
    newUser["labels"] = labels

    print(db.User.insert_one(newUser))
    return db.collection_names()
