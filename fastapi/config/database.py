from pymongo import MongoClient

# Create a new client and connect to the server
client = MongoClient("mongodb+srv://LearnMongo:Learn1234@learnmongo.i7rby.mongodb.net/?retryWrites=true&w=majority&appName=learnmongo")

# Access the 'mail_db' database (it will be created if it doesn't exist when data is first stored)
db = client.mail_db

# Access the 'mail_collection' collection within the 'mail_db' database (it will be created if it doesn't exist when data is first stored)
collection_name = db["mail_collection"]