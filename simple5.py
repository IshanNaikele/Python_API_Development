from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/sqlalchemy")
def root(db:Session = Depends(get_db)):
    return {"Connection":"Successful"}