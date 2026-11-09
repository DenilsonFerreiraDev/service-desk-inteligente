import google.generativeai as genai

from app.core.config import settings


genai.configure(
    api_key=settings.gemini_api_key
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def sugerir_solucao_gemini(
    descricao: str
):

    prompt = f"""
    Você é um analista experiente de Service Desk.

    Analise o chamado abaixo e responda somente com uma sugestão técnica de solução.

    Chamado:
    {descricao}
    """

    resposta = model.generate_content(
        prompt
    )

    return resposta.text