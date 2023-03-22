from typing import Optional

from pydantic import BaseModel, Extra


class BankCreate(BaseModel):
    name: str
    description: Optional[str]

    class Config:
        extra = Extra.forbid
        min_anystr_length = 1
