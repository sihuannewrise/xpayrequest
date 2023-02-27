from enum import Enum


class StatusBase(str, Enum):
    ACTIVE = 'действующая'
    LIQUIDATING = 'ликвидируется'
    LIQUIDATED  = 'ликвидирована'
