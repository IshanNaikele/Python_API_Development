from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
app = FastAPI()


class Post(BaseModel):
    role:str
    salary:int
    hasSkill:bool


@app.get('/')
async def root():
    return {"message":"Hello Man ,What's going on?"}

@app.post('/login')
async def root(new_post: Post):
    print(new_post.salary)
    return {"content":"Success"}

@app.post('/login')
async def root(new_post: Post):
    print(new_post.salary)
    return {"content":"Success"}


 