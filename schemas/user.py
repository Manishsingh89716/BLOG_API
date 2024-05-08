'''
create the schema of the database which stored information also as API
'''


#define functions for the blog schema
def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "title":item["title"],
        "content":item["content"],
        "author":item["author"]
    }


#define funtions to arrange the item in a sequence
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]
#Best way

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]