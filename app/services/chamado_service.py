from app.models.chamado import Chamado
from app.models.historico import Historico
from app.services.classificacao_service import classificar_chamado
from app.services.prioridade_service import definir_prioridade
from app.services.sla_service import calcular_sla
from app.services.base_conhecimento_service import (
    buscar_solucao_por_texto
)
from datetime import datetime
from datetime import timedelta
from app.services.gemini_service import (
    sugerir_solucao_gemini
)



def criar_chamado(db, dados):

    categoria = classificar_chamado(
        dados.descricao
    )

    prioridade = definir_prioridade(
        categoria
    )

    prazo_sla = calcular_sla(
        prioridade
    )

    artigo = buscar_solucao_por_texto(
        db,
        dados.descricao
    )

    if artigo:

        print(
            "Solução encontrada na Base de Conhecimento."
        )

        sugestao_solucao = artigo.solucao

    else:

        try:

            print(
                "KB não encontrou solução. Consultando Gemini..."
            )

            sugestao_solucao = sugerir_solucao_gemini(
                dados.descricao
            )

            print(
                "Sugestão gerada pelo Gemini."
            )

        except Exception as erro:

            print(
                f"Erro ao consultar Gemini: {erro}"
            )

            sugestao_solucao = (
                "Não foi possível gerar "
                "sugestão automática."
            )

    chamado = Chamado(
        solicitante=dados.solicitante,
        email=dados.email,
        descricao=dados.descricao,
        categoria=categoria,
        prioridade=prioridade,
        status="aberto",
        prazo_sla=prazo_sla,
        sugestao_solucao=sugestao_solucao
    )

    db.add(chamado)

    db.commit()

    db.refresh(chamado)

    historico = Historico(
        chamado_id=chamado.id,
        evento="Chamado criado"
    )

    db.add(historico)

    db.commit()

    return chamado


def atualizar_status(
        db,
        chamado_id,
        novo_status
):

    chamado = (
        db.query(Chamado)
        .filter(Chamado.id == chamado_id)
        .first()
    )

    if not chamado:
        return None

    chamado.status = novo_status

    historico = Historico(
        chamado_id=chamado.id,
        evento=f"Status alterado para {novo_status}"
    )

    db.add(historico)

    db.commit()

    db.refresh(chamado)

    return chamado


def buscar_chamados_sla_risco(db):

    agora = datetime.utcnow()

    limite = agora + timedelta(hours=2)

    chamados = (
        db.query(Chamado)
        .filter(
            Chamado.status != "resolvido",
            Chamado.prazo_sla <= limite
        )
        .all()
    )

    return chamados