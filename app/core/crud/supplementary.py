from app.core.crud.base import CRUDBase
from app.core.models._common import (
    SupplementaryBase
)


class SupplementaryCRUD(CRUDBase):
    pass


supplementary_crud = SupplementaryCRUD(SupplementaryBase)
