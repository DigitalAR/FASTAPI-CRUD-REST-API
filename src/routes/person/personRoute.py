from fastapi import APIRouter
from src.models.person.personModel import PersonModel
from src.controllers.person.personController import PersonController

person_router = APIRouter()
person_controller = PersonController()


@person_router.post("/person")
async def create(person: PersonModel):
    return await person_controller.create(person)
