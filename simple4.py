from fastapi import FastAPI, Response, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Dict, List
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

# 1. Corrected Pydantic model for consistency
class Post(BaseModel):
    name: str
    price: int
    id: int
    is_sale: bool

# Corrected database connection with host name
try:
    conn = psycopg2.connect(host="localhost", database='FastAPI', user='postgres', password='23062004#Ishan', cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    print("Database connected Successfully")
except Exception as e:
    print("DataBase Connection Failed")
    print(e)


# Helper functions with consistent 'id' parameter
def find_posts(lis: List[Dict], id: int):
    for i in lis:
        if i['id'] == id:
            return i
    return None

def find_posts_index(lis: List[Dict], id: int):
    for i, j in enumerate(lis):
        if j['id'] == id:
            return i
    return None

def delete_posts(lis: List[Dict], id: int):
    for i in lis:
        if i['id'] == id:
            lis.remove(i)
            print("Deleted Successfully")
            return {"Status": "Post Deleted Successfully"}
    return None

my_posts = [
    {
        "name": "Fridge",
        "price": 340,
        "id": 201,
        "is_sale": True
    },
    {
        "name": "Cooler",
        "price": 120,
        "id": 202,
        "is_sale": True
    },
    {
        "name": "Iron",
        "price": 210,
        "id": 203,
        "is_sale": False
    }
]

@app.get('/')
async def root():
    return {"message": "Hello Man, What's going on?"}

@app.get('/login')
async def get_all_products():
    cursor.execute("SELECT * FROM products")
    posts = cursor.fetchall()
    return {"content": posts}

@app.post('/login')
async def create_product(new_post: Post):
    try:
        cursor.execute(
            """INSERT INTO products (name, price, is_sale) VALUES (%s, %s, %s) RETURNING *""",
            (new_post.name, new_post.price, new_post.is_sale)
        )
        post_dict = cursor.fetchone()
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=f"Database error: {e}")
    return {"content": post_dict}

# Corrected path parameter syntax and function name
@app.get("/login/:{id}")
async def get_single_product(id: int):
    cursor.execute("SELECT * FROM products WHERE id = %s", (str(id),))
    post = cursor.fetchone()
    if not post:
        raise HTTPException(status_code=404, detail=f"Product with id {id} was not found")
    return {"post_detail": post}

# Corrected path parameter syntax and function name
@app.delete("/login/:{id}")
async def delete_product(id: int):
    cursor.execute("DELETE FROM products WHERE id = %s RETURNING *", (str(id),))
    deleted_post = cursor.fetchone()
    conn.commit()
    if not deleted_post:
        raise HTTPException(status_code=404, detail=f"Product with id {id} was not found")
    return {"status": "Product deleted successfully"}

# Corrected path parameter syntax and function name
@app.put("/login/:{id}")
async def update_product(id: int, updated_post: Post):
    cursor.execute(
        """UPDATE products SET name = %s, price = %s, is_sale = %s WHERE id = %s RETURNING *""",
        (updated_post.name, updated_post.price, updated_post.is_sale, str(id))
    )
    updated_record = cursor.fetchone()
    conn.commit()
    if not updated_record:
        raise HTTPException(status_code=404, detail=f"Product with id {id} was not found")
    return {"post_detail": updated_record}