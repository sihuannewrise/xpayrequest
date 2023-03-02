from enum import Enum

from app.core.schemas._common import StatusBase


class OPFType(str, Enum):
    BANK = 'банк'
    BANK_BRANCH = 'филиал банка'
    NKO = 'небанковская кредитная организация (НКО)'
    NKO_BRANCH = 'филиал НКО'
    RKC = 'расчетно-кассовый центр'
    CBR = 'управление ЦБ РФ (март 2021)'
    TREASURY = 'управление Казначейства (март 2021)'
    OTHER = 'другой'


class BankStatus(StatusBase):
    pass
