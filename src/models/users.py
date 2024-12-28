import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import String, func, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base_model import BaseModel


class User(SQLAlchemyBaseUserTable[int], BaseModel):
    first_name: Mapped[str] = mapped_column(String(150), nullable=True)
    last_name: Mapped[str] = mapped_column(String(150), nullable=True)
    last_login: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True), server_default=func.now(), nullable=True
    )
