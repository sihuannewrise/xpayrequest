from enum import Enum

from app.core.schemas.common import StatusBase


class CounterAgentType(str, Enum):
    LEGAL = 'юридическое лицо'
    INDIVIDUAL = 'индивидуальный предприниматель'


class CounterAgentStatus(StatusBase):
    BANKRUPT = 'банкротство'
    REORGANIZING = 'в процессе присоединения к другому юрлицу, с последующей ликвидацией'
