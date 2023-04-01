from http import HTTPStatus
from fastapi import HTTPException


class BankException(HTTPException):
    pass


class BankNotFoundError(BankException):
    def __init__(self):
        self.status_code = HTTPStatus.NOT_FOUND
        self.detail = "BIC Not Found"


class BankAlreadyExistsError(BankException):
    def __init__(self):
        self.status_code = HTTPStatus.CONFLICT
        self.detail = "BIC Already Exists"
