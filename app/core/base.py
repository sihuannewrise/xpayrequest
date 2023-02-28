"""Импорты класса Base и всех моделей для Alembic."""
from app.core.db import Base, EntityBase  # noqa
from app.core.models.bank import Banks  # noqa
from app.core.models.counteragent import CounterAgents  # noqa
from app.core.models.payer import Payers  # noqa
