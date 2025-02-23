from pymongo import MongoClient

client = MongoClient("mongodb+srv://LearnMongo:Learn1234@learnmongo.i7rby.mongodb.net/?retryWrites=true&w=majority&appName=learnmongo")

db = client.mail_db

collection_name = db["mail_collection"]