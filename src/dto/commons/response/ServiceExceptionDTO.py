class ServiceException(Exception):
    def __init__(self, message, apiError):
        self.message = message
        self.apiError = apiError
