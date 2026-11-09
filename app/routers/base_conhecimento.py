from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.models.base_conhecimento import BaseConhecimento

from app.schemas.base_conhecimento import (
    BaseConhecimentoCreate,
    BaseConhecimentoUpdate,
    BaseConhecimentoResponse
)

from app.services.base_conhecimento_service import (
    buscar_solucao_por_texto
)

router = APIRouter(
    prefix="/kb",
    tags=["Base de Conhecimento"]
)


@router.post(
    "",
    response_model=BaseConhecimentoResponse
)
def criar_artigo(
    dados: BaseConhecimentoCreate,
    db: Session = Depends(get_db)
):
    artigo = BaseConhecimento(**dados.model_dump())

    db.add(artigo)
    db.commit()
    db.refresh(artigo)

    return artigo


@router.get(
    "",
    response_model=list[BaseConhecimentoResponse]
)
def listar_artigos(
    db: Session = Depends(get_db)
):
    return db.query(BaseConhecimento).all()


@router.get("/buscar-solucao")
def buscar_solucao(
    texto: str,
    db: Session = Depends(get_db)
):
    artigo = buscar_solucao_por_texto(
        db,
        texto
    )

    if not artigo:
        return {
            "mensagem": "Nenhuma solução encontrada"
        }

    return {
        "titulo": artigo.titulo,
        "categoria": artigo.categoria,
        "solucao": artigo.solucao
    }


@router.get(
    "/{artigo_id}",
    response_model=BaseConhecimentoResponse
)
def buscar_artigo(
    artigo_id: int,
    db: Session = Depends(get_db)
):
    artigo = (
        db.query(BaseConhecimento)
        .filter(BaseConhecimento.id == artigo_id)
        .first()
    )

    if not artigo:
        raise HTTPException(
            status_code=404,
            detail="Artigo não encontrado"
        )

    return artigo


@router.put(
    "/{artigo_id}",
    response_model=BaseConhecimentoResponse
)
def atualizar_artigo(
    artigo_id: int,
    dados: BaseConhecimentoUpdate,
    db: Session = Depends(get_db)
):
    artigo = (
        db.query(BaseConhecimento)
        .filter(BaseConhecimento.id == artigo_id)
        .first()
    )

    if not artigo:
        raise HTTPException(
            status_code=404,
            detail="Artigo não encontrado"
        )

    for campo, valor in dados.model_dump().items():
        setattr(artigo, campo, valor)

    db.commit()
    db.refresh(artigo)

    return artigo


@router.delete("/{artigo_id}")
def excluir_artigo(
    artigo_id: int,
    db: Session = Depends(get_db)
):
    artigo = (
        db.query(BaseConhecimento)
        .filter(BaseConhecimento.id == artigo_id)
        .first()
    )

    if not artigo:
        raise HTTPException(
            status_code=404,
            detail="Artigo não encontrado"
        )

    db.delete(artigo)
    db.commit()

    return {
        "mensagem": "Artigo removido com sucesso"
    }