from fastapi import APIRouter, Depends

from models.user import User

from config.db import get_db
from schemas.user import serialize_dict, serialize_list
from bson import ObjectId

from motor.motor_asyncio import AsyncIOMotorClient

user = APIRouter()

@user.get('/')
async def find_all_users(conn:AsyncIOMotorClient = Depends(get_db)):
    data = await conn.local.user.find().to_list(1000)
    entity = serialize_list(data)
    return entity

@user.get('/{id}')
async def get_user(id,conn:AsyncIOMotorClient = Depends(get_db)):
    return serialize_dict(await conn.local.user.find_one(
        {"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user: User,conn:AsyncIOMotorClient = Depends(get_db)):
    await conn.local.user.insert_one(dict(user))
    return serialize_list(await conn.local.user.find().to_list(1000))

@user.put('/{id}')
async def update_user(id, user: User,conn:AsyncIOMotorClient = Depends(get_db)):
    await conn.local.user.find_one_and_update(
        {"_id":ObjectId(id)},
        {
        "$set":dict(user)
    })
    
    return serialize_dict(await conn.local.user.find_one({"_id":ObjectId(id)}))

@user.delete('/{id}')
async def delete_user(id,conn:AsyncIOMotorClient = Depends(get_db)):
    return serialize_dict(await conn.local.user.find_one_and_delete(
        {"_id":ObjectId(id)}))
    
     