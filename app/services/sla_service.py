from datetime import datetime
from datetime import timedelta


def calcular_sla(prioridade: str):

    agora = datetime.utcnow()

    if prioridade == "Alta":
        return agora + timedelta(hours=4)

    if prioridade == "Média":
        return agora + timedelta(hours=8)

    return agora + timedelta(hours=24)