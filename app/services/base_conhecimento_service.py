from sqlalchemy.orm import Session

from app.models.base_conhecimento import BaseConhecimento


def buscar_solucao_por_texto(
    db: Session,
    texto: str
):
    artigos = db.query(
        BaseConhecimento
    ).all()

    texto = texto.lower()

    palavras_texto = set(
        texto.split()
    )

    melhor_artigo = None
    maior_pontuacao = 0

    for artigo in artigos:

        palavras_artigo = set()

        palavras_artigo.update(
            artigo.titulo.lower().split()
        )

        palavras_artigo.update(
            artigo.problema.lower().split()
        )

        pontuacao = len(
            palavras_texto.intersection(
                palavras_artigo
            )
        )

        if pontuacao > maior_pontuacao:
            maior_pontuacao = pontuacao
            melhor_artigo = artigo

    print(
        f"Melhor artigo: "
        f"{melhor_artigo.titulo if melhor_artigo else 'Nenhum'} "
        f"- Pontuação: {maior_pontuacao}"
    )

    if maior_pontuacao >= 2:
        return melhor_artigo

    return None