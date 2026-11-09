from datetime import datetime

from pydantic import BaseModel


class BaseConhecimentoCreate(BaseModel):
    titulo: str
    categoria: str
    problema: str
    solucao: str


class BaseConhecimentoUpdate(BaseModel):
    titulo: str
    categoria: str
    problema: str
    solucao: str


class BaseConhecimentoResponse(BaseModel):
    id: int
    titulo: str
    categoria: str
    problema: str
    solucao: str
    created_at: datetime

    class Config:
        from_attributes = True