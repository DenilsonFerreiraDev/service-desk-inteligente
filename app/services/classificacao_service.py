def classificar_chamado(descricao: str):

    descricao = descricao.lower()

    palavras_rede = [
        "vpn",
        "wifi",
        "wi-fi",
        "internet",
        "rede",
        "dns",
        "ip"
    ]

    palavras_acesso = [
        "senha",
        "login",
        "acesso",
        "autenticação"
    ]

    palavras_hardware = [
        "impressora",
        "monitor",
        "mouse",
        "teclado",
        "notebook"
    ]

    palavras_software = [
        "outlook",
        "excel",
        "word",
        "teams",
        "sistema"
    ]

    for palavra in palavras_rede:
        if palavra in descricao:
            return "Rede"

    for palavra in palavras_acesso:
        if palavra in descricao:
            return "Acesso"

    for palavra in palavras_hardware:
        if palavra in descricao:
            return "Hardware"

    for palavra in palavras_software:
        if palavra in descricao:
            return "Software"

    return "Não Classificado"