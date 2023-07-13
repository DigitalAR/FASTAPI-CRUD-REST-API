from fastapi import HTTPException
from fastapi.responses import JSONResponse
from src.dto.commons.response.GeneralResponseDTO import GeneralResponse

class CustomHTTPException(HTTPException):
    def __init__(self, status_code: int, general_response: GeneralResponse):
        self.status_code = status_code
        self.general_response = general_response

    @property
    def response(self):
        return JSONResponse(
            status_code=self.status_code,
            content=self.general_response.dict(),
        )
