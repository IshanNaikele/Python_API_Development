from fastapi import FastAPI
from fastapi.params import Body
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/intern")
async def root_user():
    return {"Internship": "Success"}

@app.post("/job")
async def root_user(payload :dict = Body(...)):
    print(payload)
    return {"Job": ">=18 LPA"} 

@app.post("/firstJob")
async def root_user(payload :dict = Body(...)):
    print(payload)
    return payload