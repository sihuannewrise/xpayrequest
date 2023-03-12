"""Импорты класса Base и всех моделей для Alembic."""
from app.core.db import Base                            # noqa
from app.core.models import (                           # noqa
    Bank, BankAccount, CounterAgent, PaymentRequest,
    PaymentRegister, Payer, User,
    BankAccountType, PaymentType, KFP,
    PayerStatus, KBK, OKTMO, Prepayment, PaymentStatus,
    AccessToken,
)
