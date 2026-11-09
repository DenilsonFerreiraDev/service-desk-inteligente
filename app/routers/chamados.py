from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.core.database import get_db

from app.schemas.chamado import (
    ChamadoCreate,
    ChamadoResponse,
    StatusUpdate
)

from app.services.chamado_service import (
    criar_chamado,
    atualizar_status,
    buscar_chamados_sla_risco
)

from app.models.chamado import Chamado

router = APIRouter(
    prefix="/chamados",
    tags=["Chamados"]
)

@router.get("/teste")
def teste():
    return {
        "mensagem": "rota teste funcionando"
    }

@router.post(
    "",
    response_model=ChamadoResponse
)
def novo_chamado(
    dados: ChamadoCreate,
    db: Session = Depends(get_db)
):
    return criar_chamado(db, dados)


@router.get(
    "/listar-teste",
    response_model=list[ChamadoResponse]
)
def listar_chamados(
    db: Session = Depends(get_db)
):
    return db.query(Chamado).all()


@router.get(
    "/monitoramento/sla-risco",
    response_model=list[ChamadoResponse]
)
def sla_risco(
    db: Session = Depends(get_db)
):
    return buscar_chamados_sla_risco(db)


@router.get(
    "/{chamado_id}",
    response_model=ChamadoResponse
)
def buscar_chamado(
    chamado_id: int,
    db: Session = Depends(get_db)
):

    chamado = (
        db.query(Chamado)
        .filter(Chamado.id == chamado_id)
        .first()
    )

    if not chamado:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    return chamado


@router.patch(
    "/{chamado_id}/status",
    response_model=ChamadoResponse
)
def alterar_status(
    chamado_id: int,
    dados: StatusUpdate,
    db: Session = Depends(get_db)
):

    chamado = atualizar_status(
        db,
        chamado_id,
        dados.status
    )

    if not chamado:
        raise HTTPException(
            status_code=404,
            detail="Chamado não encontrado"
        )

    return chamado