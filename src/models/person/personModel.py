from pydantic import BaseModel
from typing import Text, Optional
from datetime import date, datetime


class PersonModel(BaseModel):
    name: str
    surname: str
    birthdate: Optional[date]
