from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func

from app.core.database import Base


class BaseConhecimento(Base):
    __tablename__ = "base_conhecimento"

    id = Column(Integer, primary_key=True, index=True)

    titulo = Column(String(200), nullable=False)

    categoria = Column(String(100), nullable=False)

    problema = Column(Text, nullable=False)

    solucao = Column(Text, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )