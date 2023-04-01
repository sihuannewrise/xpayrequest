from fastapi import HTTPException


class BankException(HTTPException):
    ...


class BankNotFoundError(BankException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Bank Not Found"


class BankAlreadyExistsError(BankException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Bank Already Exists"
