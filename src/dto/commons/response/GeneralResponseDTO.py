from pydantic import BaseModel
from typing import Optional


class GeneralResponse(BaseModel):
    data: Optional[dict] = None
    success: bool = True
    message: str = "Proceso Correcto"
    apiError: Optional[dict] = None
