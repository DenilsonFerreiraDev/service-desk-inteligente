from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class Chamado(Base):
    __tablename__ = "chamados"

    id = Column(Integer, primary_key=True, index=True)

    solicitante = Column(String(100))

    email = Column(String(120))

    descricao = Column(String(1000))

    categoria = Column(String(50))

    prioridade = Column(String(20))

    status = Column(
        String(30),
        default="aberto"
    )

    criado_em = Column(
        DateTime,
        default=datetime.utcnow
    )

    prazo_sla = Column(DateTime)

    resolvido_em = Column(DateTime)

    sugestao_solucao = Column(String(2000))