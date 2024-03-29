from typing import Optional
from fastapi import Body, FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


my_posts = [{"title" : "title of post 1", "content" : "content of post 1", "id" : 1}, 
            {"title" : "My favorite food", "content" : "I like to eat food called pussy", "id" : 2 }]

@app.get("/")
async def root():
    return {"message": "Hello Bitch"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post:Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"Data":post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    print(post)
    return{"post_detail" : post}
