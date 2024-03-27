from fastapi import Body, FastAPI
from fastapi.params import Body


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello Bitch"}

@app.get("/posts")
def get_posts():
    return {"data": "This is your posts"}

@app.post("/createposts")
def create_posts(body: dict = Body(...)):
    print(body)
    return {"new_post": f"title {body['title']} content: {body['content']}"}

