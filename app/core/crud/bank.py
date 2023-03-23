from app.core.crud.base import CRUDBase
from app.core.models.bank import Bank


class BankCRUD(CRUDBase):
    pass


bank_crud = BankCRUD(Bank)
