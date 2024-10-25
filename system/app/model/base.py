from datetime import datetime, timezone
from typing import Dict, Any

from sqlalchemy import TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, mapped_column


class ElsaBaseModel(DeclarativeBase):
    def as_dict(self) -> Dict[str, Any]:
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
        }

    def as_updatable_dict(self) -> Dict[str, Any]:
        return {
            column.name: getattr(self, column.name) for column in self.__table__.columns
            if column.name not in {'id', 'created_on', 'last_modified_on'}
        }

    created_on = mapped_column(TIMESTAMP(timezone=True), nullable=False, default=datetime.now(tz=timezone.utc))
    last_modified_on = mapped_column(TIMESTAMP(timezone=True),
                                     nullable=False,
                                     default=datetime.now(tz=timezone.utc),
                                     onupdate=datetime.now(tz=timezone.utc))
