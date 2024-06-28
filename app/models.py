from flask import current_app
from pymongo import MongoClient

db = None
tokens_collection = None

def init_db(app):
    global db
    global tokens_collection
    client = MongoClient(app.config['MONGO_URI'])
    db = client.get_database('DBRecruitment')  # Update to use get_database method
    tokens_collection = db.get_collection('SocialMedia_Tokens')  # Update to use get_collection method
