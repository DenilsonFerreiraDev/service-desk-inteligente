from fastapi import APIRouter

from app.services.gemini_service import (
    sugerir_solucao_gemini
)

router = APIRouter(
    prefix="/gemini",
    tags=["Gemini"]
)


@router.get("/teste")
def teste_gemini(
    texto: str
):
    resposta = sugerir_solucao_gemini(
        texto
    )

    return {
        "resposta": resposta
    }