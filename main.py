from fastapi import FastAPI
from pydantic import BaseModel
from model import Product
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:5173'],
    allow_methods=["*"],
    allow_headers=["*"],
)


products=[
    Product(id=1,name="subodh",age=24),
    Product(id=2,name="Hari",age=23),
    Product(id=3,name="Gopal",age=25)
]

@app.get("/")
def return_produt():
    return {"message":"Main Page loaded"}


@app.get("/products")
def get_all_products():
    return products


@app.get("/products/{id}")
def get_product_by_id(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            return products[i]

@app.put("/products/{id}")
def update_product(id:int,product:Product):
    for i in range(len(products)):
        if products[i].id==id:
            products[i]=product
            return product
    
    return {"Product Not found"}


@app.post("/products")
def add_product(product:Product):
    products.append(product)
    return {"Product added Successfully"}


@app.delete("/products/{id}")
def delete_product(id:int):
    for i in range(len(products)):
        if products[i].id==id:
            del products[i]
            return {"Product Deleted Sucessfully"}

    return {"Product Not found"}

