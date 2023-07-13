from pydantic import BaseModel
from typing import Optional
from src.utils.constants.httpCodes import BAD_REQUEST


class ApiError(BaseModel):
    messageUser: Optional[str] = "Proceso Fallído. Por favor intente más tarde"
    messageDeveloper: Optional[str] = None
    code: Optional[str] = "ERR-00"
    codeHTTP: Optional[int] = BAD_REQUEST
