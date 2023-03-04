from datetime import datetime
from typing_extensions import Annotated

from sqlalchemy import func, String
from sqlalchemy.orm import mapped_column


class AnnonationSettings:
    intpk = Annotated[int, mapped_column(primary_key=True)]
    timestamp = Annotated[
        datetime,
        mapped_column(
            nullable=False,
            server_default=func.CURRENT_TIMESTAMP()),
    ]
    str_50 = Annotated[str, mapped_column(String(50), nullable=False)]


ans = AnnonationSettings()
