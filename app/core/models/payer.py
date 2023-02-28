from sqlalchemy import Column, ForeignKey, Integer, String

from app.core.db import Base


class Payers(Base):
    ca_id = Column(
        Integer,
        ForeignKey(
            'counteragents.id',
            ondelete='CASCADE',
        ),
        unique=True,
        nullable=False,
    )
    name = Column(
        String(20),
        unique=True,
        nullable=False,
    )
