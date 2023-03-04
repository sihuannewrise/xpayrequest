from enum import Enum


class BankOPFType(str, Enum):
    BANK = 'банк'
    BANK_BRANCH = 'филиал банка'
    NKO = 'небанковская кредитная организация (НКО)'
    NKO_BRANCH = 'филиал НКО'
    RKC = 'расчетно-кассовый центр'
    CBR = 'управление ЦБ РФ (март 2021)'
    TREASURY = 'управление Казначейства (март 2021)'
    OTHER = 'другой'


class CounterAgentType(str, Enum):
    LEGAL = 'юридическое лицо'
    INDIVIDUAL = 'индивидуальный предприниматель'


class EntityStatus(str, Enum):
    ACTIVE = 'действующая'
    LIQUIDATING = 'ликвидируется'
    LIQUIDATED = 'ликвидирована'
    BANKRUPT = 'банкротство'
    REORGANIZING = ('в процессе присоединения к другому юрлицу, '
                    'с последующей ликвидацией')
