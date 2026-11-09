from fastapi import FastAPI

from app.core.database import Base
from app.core.database import engine

from app.models.chamado import Chamado
from app.models.historico import Historico
from app.models.base_conhecimento import BaseConhecimento

from app.routers import chamados
from app.routers import base_conhecimento
from app.routers import gemini


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Service Desk Automatizado"
)

app.include_router(chamados.router)
app.include_router(base_conhecimento.router)
app.include_router(gemini.router)


@app.get("/")
def home():
    return {
        "mensagem": "Service Desk Automatizado Online"
    }