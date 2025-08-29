from fastapi import FastAPI ,Response
from fastapi.params import Body
from pydantic import BaseModel
from typing import Dict,List
from random import randrange
app = FastAPI()


class Post(BaseModel):
    Role:str
    Company:str
    Salary:int
    CompanyID:int

def find_posts(lis:List[Dict],id:int):
    for i in lis:
        print(i)
        if i['CompanyID'] ==id :
            return i
        
    return None 

def find_posts_index(lis:List[Dict],id:int):
    for i,j in enumerate(lis):
         
        if j['CompanyID'] == id:
            return i
        
    return None 

def delete_posts(lis:List[Dict],id:int):
    for i in lis:
        if i['CompanyID'] ==id :
            lis.remove(i)
            print("Deleted Successfully")
            return {"Status":"Post Deleted Successfully"}
    return None 
 

my_posts=[
    {"Role":"AI Engineer","Company":"Google","Salary":30000,"CompanyID":1},
    {"Role":"Data Science","Company":"Data Science","Salary":45000,"CompanyID":2}
        ]

@app.get('/')
async def root():
    return {"message":"Hello Man ,What's going on?"}

@app.get('/login')
async def root():
    return {"content":my_posts }

@app.post('/login')
async def root(new_post: Post):
    post_dict=new_post.dict()
    post_dict['CompanyID']=randrange(0,10000000)
    print(post_dict)
    my_posts.append(post_dict)
    print(post_dict)
    return {"content":post_dict}
 

@app.get("/login/:{CompanyID}")
async def root(CompanyID:int,response:Response):
    print(CompanyID)
    ans=find_posts(my_posts,CompanyID)
    print(ans)
    if not ans :
        response.status_code = 404
    return {"Post Detail":f"{ans}"}


@app.delete("/login/:{CompanyID}")
async def root(CompanyID:int,response:Response):
    print(CompanyID)
    ans=delete_posts(my_posts,CompanyID)
    print(ans)
    if not ans :
        response.status_code = 404
    return {"Post Detail":f"{ans}"}

@app.put("/login/:{CompanyID}")
async def update_post(CompanyID: int, updated_post: Post):
     
    index = find_posts_index(my_posts, CompanyID)
     

    updated_post_dict = updated_post.dict()
    updated_post_dict['CompanyID']=CompanyID
    my_posts[index] = updated_post_dict
    
    return {"Post Detail": updated_post_dict}