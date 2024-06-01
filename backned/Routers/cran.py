import json

from fastapi import APIRouter
from backned.Database import model, brand, stock
import pandas as pd

router = APIRouter(
    prefix="/cran",
    tags=["cran"],
)
modelDB = model.ModelDatabase()
brandDB = brand.BranDatabase()
stockDB = stock.StockDatabase()


@router.get("/stock")
async def get_brand():
    try:
        return {"message": json.loads(pd.DataFrame(stockDB.select()).to_json(orient="records"))}
    except Exception as e:
        return {"message": e}


@router.post("/stock/insert")
async def insert_stock(data: dict):
    try:
        stockDB.insert(data)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.get("/stock/delete/{id_stock:int}")
async def del_stock(id_stock: int):
    try:
        stockDB.delete(id_stock)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.post("/stock/update/{id_stock:int}")
async def update_stock(data: dict, id_stock: int):
    try:
        stockDB.update(id_stock, data)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.get("/brand")
async def get_brand():
    try:
        return {"message": json.loads(pd.DataFrame(brandDB.select()).to_json(orient="records"))}
    except Exception as e:
        return {"message": e}


@router.post("/brand/insert")
async def get_brand(data: dict):
    try:
        brandDB.insert(data)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.get("/brand/delete/{id_brand:int}")
async def del_brand(id_brand: int):
    try:
        brandDB.delete(id_brand)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.get("/model/{id_brand:int}")
async def get_model(id_brand: int):
    try:
        if id_brand:
            response = modelDB.select(id_brand)
        else:
            response = modelDB.select()
        response = pd.DataFrame(response).to_json(orient="records")
        return {"message": json.loads(response)}
    except Exception as e:
        return {"message": e}


@router.get("/model/delete/{id_brand:int}")
async def del_model(id_brand: int):
    try:
        modelDB.delete(id_brand)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.get("/model/update/{id_brand:int}")
async def get_model(id_brand: int):
    try:
        modelDB.update(id_brand, {"model": "test123"})
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.post("/model/insert")
async def get_model(data: dict):
    try:
        modelDB.insert(data)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.get("/")
async def root():
    return {"message": "Hello Mother Fucker! This is ViraKran API Cran chapter!"}
