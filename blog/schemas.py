from __future__ import annotations
from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    body: str

class Blog(BlogBase):
    model_config = {
        "from_attributes": True
    }
# for showing the results in docs
# and these models are called schemas, while the sqlalchemy objects are called models
# define the response ypu want, specify fields
class ShowBlog(BaseModel):
    title: str
    body: str
    creator: ShowUser

    model_config = {
        "from_attributes": True
    }

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    blogs: List[ShowBlog] = []

    model_config = {
        "from_attributes": True
    }