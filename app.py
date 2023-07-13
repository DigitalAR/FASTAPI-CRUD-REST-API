from fastapi import FastAPI
from src.routes.person.personRoute import person_router

app = FastAPI()

app.include_router(person_router)
