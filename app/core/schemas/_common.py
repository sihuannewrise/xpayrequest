from enum import Enum


class EntityStatusBase(str, Enum):
    ACTIVE = 'действующая'
    LIQUIDATING = 'ликвидируется'
    LIQUIDATED = 'ликвидирована'
