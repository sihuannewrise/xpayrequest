class BaseException(Exception):
    ...


class ObjectNotFoundError(BaseException):
    def __init__(self):
        self.status_code = 404
        self.detail = "Object Not Found"


class ObjectAlreadyExistsError(BaseException):
    def __init__(self):
        self.status_code = 409
        self.detail = "Object Already Exists"
