from pymongo import MongoClient
import datetime
import sys

from bson.objectid import ObjectId

global con
global db
global records


def connect_db():
    global con
    global db
    global records
    con = MongoClient('mongodb+srv://priyanka:piyu31@cluster0.mdba4.mongodb.net/product_App?retryWrites=true&w=majority')
    db = con.product_App
    records = db.flask_project
    return


def save_recipe(savRcpCol):
    global records
    connect_db()
    records.insert(savRcpCol)
    return


def read():
    global records
    connect_db()
    Data = records.find({})
    print(Data)
    return Data
