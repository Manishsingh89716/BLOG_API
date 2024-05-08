#create the title, content and name of author using OOP

from pydantic import BaseModel

class User(BaseModel):
    title: str
    content: str
    author: str
