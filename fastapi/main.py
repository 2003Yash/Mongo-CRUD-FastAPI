from fastapi import FastAPI
from routes.route import router
app = FastAPI()

# below code to connect to mongo and establish a ping confirmation
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://<username>:<password>@learnmongo.i7rby.mongodb.net/?retryWrites=true&w=majority&appName=learnmongo"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
   client.admin.command('ping')
   print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
   print(e)

app.include_router(router)