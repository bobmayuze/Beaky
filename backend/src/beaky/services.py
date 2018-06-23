import requests
import json
import csv
import json
import os
import sys
import datetime
import time
from pymongo import MongoClient
from bson.objectid import ObjectId


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

def publishQuestion(question, voter_size, initial_pool, audience_labels):
    client = MongoClient('mongo_db', 27017)
    db = client["ScicatDB"]
    db.authenticate('mongoApp', 'mongoAppPass')

    newQuestion = dict()

    newQuestion["question"] = question
    newQuestion["voter_size"] = voter_size
    newQuestion["initial_pool"] = initial_pool
    newQuestion["audience_labels"] = audience_labels
    newQuestion["status"] = "open"
    newQuestion["count_true"] = 0
    newQuestion["count_false"] = 0

    result = db.Question.insert_one(newQuestion)
    return result

def voteQuestionById(question_id, choice):
    client = MongoClient('mongo_db', 27017)
    db = client["ScicatDB"]
    db.authenticate('mongoApp', 'mongoAppPass')

    current_question = db.Question.find_one({"_id": ObjectId(question_id)})
    if current_question["status"] == "close":
        return ("Question closed")
    try:
        if choice == "yes":
            db.Question.update_one({
                "_id": ObjectId(question_id),
                'status': "open"
            }, {'$inc': {
                'count_true': 1
            }})
        else:
            db.Question.update_one({
                "_id": ObjectId(question_id),
                'status': "open"
            }, {'$inc': {
                'count_false': 1
            }})

        current_question = db.Question.find_one({"_id": ObjectId(question_id)})
        current_votes = current_question["count_false"] + current_question["count_true"]
        if current_votes == current_question["voter_size"]:
            db.Question.update_one({
                "_id": ObjectId(question_id),
            }, {'$set': {
                'status': "close"
            }})
        return("Record successfully updated")
    except Exception as e:
        print(">>>>>>>>>>>>>Exception: \n",e)
        return ("Bad Request")


def getQuestionById(question_id):
    client = MongoClient('mongo_db', 27017)
    db = client["ScicatDB"]
    db.authenticate('mongoApp', 'mongoAppPass')

    returnQuestion = ""
    result = db.Question.find({"_id": ObjectId(question_id)})
    if (result.count == 0):
        return("Invalid questions, we cannot find it in the db")
    for question in result:
        returnQuestion = question

    returnQuestion["_id"] = str(returnQuestion["_id"])
    return returnQuestion



def getQuestionsByQuery(args):

    return("TODO: Not implemented yet")

def getQuestionsByLabels(labels):
    '''
    require : 
        labels: str[] -> A list of labels in string. 
    return :
        list of question objects that contains all labels
    '''
    client = MongoClient('mongo_db', 27017)
    db = client["ScicatDB"]
    db.authenticate('mongoApp', 'mongoAppPass')

    allQuestions = db.Question.find()
    relatedQuestions = []
    for question in allQuestions:
        currentLabels = question["audience_labels"]
        if (all([label in currentLabels for label in labels])):
            question["_id"] = str(question["_id"])
            relatedQuestions.append(question)
    return relatedQuestions