from fastapi import APIRouter
from models.mails import mail
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId #to identify automatic id created by mongo

router = APIRouter()

# CRUD - Create + Read + Update + Delete
 
# GET Request Method (READ)
@router.get("/")
async def get_mails():
    mails = list_serial(collection_name.find())
    return mails

# POST Request Method (CREATE)
@router.post("/")
async def post_mails(mail: mail):
    collection_name.insert_one(dict(mail))

# PUT Request Method (UPDATE)
@router.put("/{id}")
async def put_mail(id: str, mail: mail):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(mail)})

# REMOVE Request Method (DELETE)
@router.delete("/{id}")
async def delete_mail(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})