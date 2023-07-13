from fastapi import Request, Response
from src.models.person.personModel import PersonModel
from src.dto.commons.response.ServiceExceptionDTO import ServiceException
from src.dto.commons.response.ApiErrorDTO import ApiError
from src.utils.constants.httpCodes import *


class PersonService:
    async def create(self, person: PersonModel):
        try:
            print(x)  # Generar un error intencional (x no está definido)
        except Exception as error:
            raise error
            # api_error = ApiError(
            #     messageUser="Mensaje de usuario",
            #     messageDeveloper="Mensaje de desarrollador",
            #     code="ERR-001",
            #     codeHTTP=500,
            # )
            # service_exception = ServiceException("Error", api_error)
            # raise service_exception
