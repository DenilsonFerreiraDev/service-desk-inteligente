from pydantic import BaseModel
from datetime import datetime


class ChamadoCreate(BaseModel):
    solicitante: str
    email: str
    descricao: str


class ChamadoResponse(BaseModel):
    id: int
    solicitante: str
    email: str
    descricao: str

    categoria: str | None
    prioridade: str | None

    status: str

    criado_em: datetime

    sugestao_solucao: str | None = None

    class Config:
        from_attributes = True


class StatusUpdate(BaseModel):
    status: str