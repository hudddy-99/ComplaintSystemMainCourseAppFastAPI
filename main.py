from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import database
from resources.route import api_router

origins = ["http://localhost", "http://localhost:8000"]

app = FastAPI()
app.include_router(api_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def startup():
    await database.disconnect()
