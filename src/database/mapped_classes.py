import enum
from sqlalchemy.orm import Mapped,mapped_column, DeclarativeBase, declarative_base, relationship
from sqlalchemy import String, Integer, Boolean, DateTime, text, ForeignKey
from typing import Optional, List

base:DeclarativeBase = declarative_base()

class Role(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(base):
    __tablename__ = "User"

    id: Mapped[int] = mapped_column(primary_key=True)
    user: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(40))
    role:Mapped[Optional[Role]] = mapped_column(default=Role.ADMIN)
    isActive:Mapped[Optional[bool]] = mapped_column(default=True)

class Camara(base):
    __tablename__ = "Camara"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(60))
    url: Mapped[str] = mapped_column(String(150), unique=True)
    status: Mapped[bool] = mapped_column (Boolean(), default=False)
    limTop: Mapped[int] = mapped_column(Integer())
    limBut: Mapped[int] = mapped_column(Integer())
    sendTime: Mapped[int] = mapped_column(Integer())
    incidents: Mapped[List["Incidents"]] = relationship()
    notification: Mapped[List["Notification"]] = relationship()


class Incidents(base):
    __tablename__ = "Incidents"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[str] = mapped_column(DateTime, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    description: Mapped[str] = mapped_column(String(100))
    countPeople: Mapped[int] = mapped_column(Integer())
    idCamara: Mapped[int] = mapped_column(ForeignKey("Camara.id"))

class Contact(base):
    __tablename__ = "Contact"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(70), unique=True)
    notification: Mapped[List["Notification"]] = relationship()

class Notification(base):
    __tablename__ = "Notification"

    id: Mapped[int] = mapped_column(primary_key=True)
    idCamara: Mapped[int] = mapped_column(ForeignKey("Camara.id"))
    idContact: Mapped[int] = mapped_column(ForeignKey("Contact.id"))