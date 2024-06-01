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
    return {"message": pd.DataFrame(clients.select()).to_json(orient="records")}


@router.get("/clients/delete/{id}")
async def delete_clients(id_: int):
    clientDB.delete(id_)
    return {"message": True}


@router.get("/rent/{id}")
async def get_clients(id_: int):
    return {"message": pd.DataFrame(rent_app.select(id_)).to_json(orient="records")}


@router.get("/rent")
async def get_clients():
    return {"message": pd.DataFrame(rent_app.select()).to_json(orient="records")}


@router.get("/rent/delete/{id}")
async def delete_clients(id_: int):
    rentDB.delete(id_)
    return {"message": True}