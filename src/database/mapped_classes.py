import enum
from sqlalchemy.orm import Mapped,mapped_column, DeclarativeBase, declarative_base
from sqlalchemy import String
from typing import Optional

base:DeclarativeBase = declarative_base()

class Role(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String())
    role:Mapped[Optional[Role]] = mapped_column(default=Role.ADMIN)
    isActive:Mapped[Optional[bool]] = mapped_column(default=True)