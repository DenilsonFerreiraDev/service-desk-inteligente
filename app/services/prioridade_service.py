def definir_prioridade(categoria: str):

    prioridades = {
        "Rede": "Alta",
        "Acesso": "Média",
        "Software": "Média",
        "Hardware": "Baixa",
        "Não Classificado": "Baixa"
    }

    return prioridades.get(
        categoria,
        "Baixa"
    )