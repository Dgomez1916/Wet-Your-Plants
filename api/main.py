from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from routers import (
    plant_detail,
    users,
    watering_schedules,
    greenhouse,
    dashboard,
    get_plant_species,
)
from authenticator import authenticator

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        os.environ.get(
            "CORS_HOST", "http://localhost:8000"
        )
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "You hit the root path!"}


app.include_router(authenticator.router)
app.include_router(plant_detail.router)
app.include_router(users.router)
app.include_router(watering_schedules.router)
app.include_router(greenhouse.router)
app.include_router(dashboard.router)
app.include_router(get_plant_species.router)
