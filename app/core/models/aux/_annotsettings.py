# файл не используется
from datetime import datetime
from typing_extensions import Annotated

from sqlalchemy import func, text
from sqlalchemy.orm import mapped_column


class AnnonationSettings:
    timestamp = Annotated[
        datetime,
        mapped_column(
            server_default=func.CURRENT_TIMESTAMP()),
    ]

    timestamp_upd = Annotated[
        datetime,
        mapped_column(
            server_default=text(
                "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")),
    ]

    bool_0 = Annotated[
        bool,
        mapped_column(
            default=False,
            server_default=text('FALSE')),
    ]


ans = AnnonationSettings()
