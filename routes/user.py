'''
APIRouter class, used to group path operations, for example to structure an app in multiple files.
It would then be included in the FastAPI app, or in another APIRouter (ultimately included in the app).
'''

#import all accessible libraries

from fastapi import APIRouter
from models.user import User
from config.db import conn
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter()


#to get the whole API functions
@user.get('/')
async def find():
    return serializeList(conn.local.user.find())

#hit the request to get the Id
@user.get('/{id}')
async def read(id):
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))


#hit the request to create the post of the blog
@user.post('/')
async def create(user: User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())

#hit the rquest to comment on the blog
@user.post('/{id}')
async def comments(user: User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())


#hit the request to update the content of the blog
@user.put('/{id}')
async def update(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))


#hit the request to delete the content of the blog
@user.delete('/{id}')
async def delete(id,user: User):
    return serializeDict(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))