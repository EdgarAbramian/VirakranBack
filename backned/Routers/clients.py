from fastapi import APIRouter
from backned.Database import clients, rent_app
import pandas as pd

router = APIRouter(
    prefix="/clients",
    tags=["clients"],
)

clientDB = clients.ClientsDatabase()
rentDB = rent_app.RentDatabase()


@router.get("/clients")
async def get_clients():
    try:
        return {"message": pd.DataFrame(clients.select()).to_json(orient="records")}
    except Exception as e:
        return {"message": e}


@router.get("/clients/delete/{id}")
async def delete_clients(id_: int):
    try:
        clientDB.delete(id_)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.post("/clients/insert")
async def insert_clients(data: dict):
    try:
        clientDB.insert(data)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.post("/clients/update/{id}")
async def update_clients(id_: int, data: dict):
    try:
        clientDB.update(id_, data)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.get("/rent/{id}")
async def get_clients(id_: int):
    try:
        return {"message": pd.DataFrame(rent_app.select(id_)).to_json(orient="records")}
    except Exception as e:
        return {"message": e}


@router.get("/rent")
async def get_clients():
    try:
        return {"message": pd.DataFrame(rent_app.select()).to_json(orient="records")}
    except Exception as e:
        return {"message": e}


@router.get("/rent/delete/{id}")
async def delete_clients(id_: int):
    try:
        rentDB.delete(id_)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.post("/rent/insert")
async def insert_clients(data: dict):
    try:
        rentDB.insert(data)
        return {"message": True}
    except Exception as e:
        return {"message": e}


@router.post("/rent/update/{id}")
async def update_clients(id_: int, data: dict):
    try:
        rentDB.update(id_, data)
        return {"message": True}
    except Exception as e:
        return {"message": e}
