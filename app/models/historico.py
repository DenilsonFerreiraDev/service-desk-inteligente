from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from app.core.database import Base


class Historico(Base):
    __tablename__ = "historico"

    id = Column(Integer, primary_key=True)

    chamado_id = Column(Integer)

    evento = Column(String(255))

    data = Column(
        DateTime,
        default=datetime.utcnow
    )