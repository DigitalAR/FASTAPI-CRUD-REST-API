from fastapi import HTTPException
from src.services.person.personService import PersonService
from src.dto.commons.response.GeneralResponseDTO import GeneralResponse
from src.dto.commons.response.ApiErrorDTO import ApiError
from src.dto.commons.response.ServiceExceptionDTO import ServiceException
from src.utils.constants.httpCodes import *
from src.models.person.personModel import PersonModel


class PersonController:
    def __init__(self):
        self.person_service = PersonService()

    async def create(self, person: PersonModel):
        try:
            data = await self.person_service.create(person)
            general_response = GeneralResponse(data=data)
            return general_response
        except ServiceException as error:
            api_error = error.apiError.dict()
            http_code = api_error["codeHTTP"]
            general_response = GeneralResponse(
                success=False, message=error.message, apiError=api_error
            )
            raise HTTPException(
                status_code=http_code, detail=general_response.model_dump()
            )
        except Exception as error:
            api_error = ApiError(
                messageDeveloper=str(error),
            )
            general_response = GeneralResponse(
                success=False,
                message=api_error.messageUser,
                apiError=api_error.model_dump(),
            )
            raise HTTPException(
                status_code=BAD_REQUEST, detail=general_response.model_dump()
            )
